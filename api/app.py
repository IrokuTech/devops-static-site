import os
import time

import psycopg2
from flask import Flask, jsonify, request
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Histogram,
    generate_latest,
)

app = Flask(__name__)


REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status"],
)

REQUEST_ERRORS = Counter(
    "http_request_errors_total",
    "Total number of HTTP requests returning an error",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
)


def get_db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


def initialize_database():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY,
            count INTEGER NOT NULL
        );
        """
    )

    cursor.execute(
        """
        INSERT INTO visits (id, count)
        VALUES (1, 0)
        ON CONFLICT (id) DO NOTHING;
        """
    )

    connection.commit()
    cursor.close()
    connection.close()


@app.before_request
def start_timer():
    request.start_time = time.perf_counter()


@app.after_request
def record_metrics(response):
    if request.path == "/metrics":
        return response

    duration = time.perf_counter() - request.start_time
    endpoint = request.url_rule.rule if request.url_rule else "unknown"

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        status=response.status_code,
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=endpoint,
    ).observe(duration)

    if response.status_code >= 400:
        REQUEST_ERRORS.labels(
            method=request.method,
            endpoint=endpoint,
            status=response.status_code,
        ).inc()

    return response


@app.route("/health")
def health():
    return jsonify(status="healthy")


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


@app.route("/api/visits")
def visits():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE visits
        SET count = count + 1
        WHERE id = 1
        RETURNING count;
        """
    )

    visit_count = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return jsonify(visits=visit_count)


if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=8000)
