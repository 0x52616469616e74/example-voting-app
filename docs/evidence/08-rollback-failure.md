# Controlled failure evidence

A Helm upgrade set `global.imageTag=rollback-demo-missing`. Kubernetes retained
the healthy ReplicaSets while the new ReplicaSets failed to pull the nonexistent
immutable tag.

```text
result (new ReplicaSet)  READY=false  WAITING=ErrImagePull
vote   (new ReplicaSet)  READY=false  WAITING=ErrImagePull
worker (new ReplicaSet)  READY=false  WAITING=ErrImagePull

Healthy SHA-tagged ReplicaSets remained Ready during the drill.
```

No production image or registry tag was altered for this test.

