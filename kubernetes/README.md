# Kubernetes local lab

Local Kubernetes learning lab using Kind.

## Resources

* Namespace: `devops-lab`
* ConfigMap: `nginx-config`
* Secret: `nginx-secret`
* Deployment: `nginx-demo`
* Service: `nginx-service`

## Create the lab

Create the namespace and configuration:

```bash
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/configmap.yaml
```

Create the Secret locally:

```bash
kubectl create secret generic nginx-secret \
  --from-literal=DEMO_PASSWORD='change-me' \
  -n devops-lab
```

The Secret is created directly in the cluster and must not be committed to Git.

`kubernetes/secret.example.yaml` only documents the expected structure. Replace the example value with a local value when creating the real Secret.

Apply the Deployment and Service:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

## Verify the lab

Check the resources:

```bash
kubectl get all -n devops-lab
kubectl get configmap nginx-config -n devops-lab
kubectl get secret nginx-secret -n devops-lab
```

Check the Deployment rollout:

```bash
kubectl rollout status deployment/nginx-demo -n devops-lab
```

Inspect the Pods:

```bash
kubectl get pods -n devops-lab
```

Inspect the Service and its endpoints:

```bash
kubectl get service nginx-service -n devops-lab
kubectl get endpointslice -n devops-lab
```

## Local access

Forward the Kubernetes Service to the host:

```bash
kubectl port-forward service/nginx-service 8082:80 -n devops-lab
```

Keep this command running in its terminal.

From another terminal, verify the response:

```bash
curl http://localhost:8082
```

Stop the port-forward with `Ctrl+C` when finished.

## Important: local Secret handling

Do not commit real credentials or `kubernetes/secret.yaml` to Git.

The repository contains `kubernetes/secret.example.yaml` only as an example. Its placeholder value is not intended to be deployed.

Do not run:

```bash
kubectl apply -f kubernetes/
```

while `secret.example.yaml` remains in the directory, because Kubernetes would also apply the example Secret with its placeholder value.

Apply the manifests individually in the documented order instead.
