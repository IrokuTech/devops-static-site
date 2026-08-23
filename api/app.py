import os

import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


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


@app.route("/health")
def health():
    return jsonify(status="healthy")


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
