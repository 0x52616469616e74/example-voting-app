# Helm rollback demonstration

This exercise proves that a failed application release can be detected and safely reversed without modifying infrastructure.

## 1. Confirm the healthy revision

```bash
helm list --namespace voting-app
kubectl get pods --namespace voting-app
helm history voting-app --namespace voting-app
```

Record the current revision number and capture evidence with no secrets visible.

## 2. Introduce a controlled failure

Deploy an image tag that does not exist. `--atomic` automatically rolls back if the rollout cannot become ready:

```bash
helm upgrade voting-app ./voting-app \
  --namespace voting-app \
  --set global.imageTag=rollback-demo-missing \
  --reuse-values \
  --atomic --timeout 3m
```

The command should fail because Kubernetes cannot pull the image. Capture the failed rollout event.

## 3. Verify recovery

```bash
helm history voting-app --namespace voting-app
kubectl get pods --namespace voting-app
kubectl rollout status deployment/voting-app-voting-app-vote --namespace voting-app
kubectl rollout status deployment/voting-app-voting-app-result --namespace voting-app
kubectl rollout status deployment/voting-app-voting-app-worker --namespace voting-app
```

If a release was created without `--atomic`, restore the last healthy revision explicitly:

```bash
helm rollback voting-app <healthy-revision> --namespace voting-app --wait
```

## Evidence to retain

- Healthy pods before the exercise.
- The controlled failed deployment and `ImagePullBackOff` event.
- Helm history showing the failed or rolled-back revision.
- Healthy pods and application screens after recovery.
