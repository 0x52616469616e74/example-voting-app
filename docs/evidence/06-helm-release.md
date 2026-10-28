# Live Helm release evidence

Captured on 2026-10-28. The demonstration used ephemeral PostgreSQL storage
(`postgresql.persistence.enabled=false`) because the temporary EKS cluster did
not install the EBS CSI driver. Production deployments should retain the chart
default of persistent storage.

```text
NAME: voting-app
NAMESPACE: voting-app
STATUS: deployed
CHART: voting-app-0.1.0

NAME                                            READY  STATUS
voting-app-voting-app-postgres-0                1/1    Running
voting-app-voting-app-redis-*                   1/1    Running
voting-app-voting-app-result-*                  1/1    Running
voting-app-voting-app-vote-*                    1/1    Running
voting-app-voting-app-worker-*                  1/1    Running
```

All application workloads used immutable GHCR tag
`e30553c367c3c9cddc4661050ebe234bc20af383`.

