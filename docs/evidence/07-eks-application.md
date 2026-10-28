# EKS application-flow evidence

The Vote and Result services were reached through local `kubectl port-forward`
connections to the EKS services on 2026-10-28.

```text
Vote landing HTTP: 200
Vote A POST HTTP: 200; selected=True
Vote B POST HTTP: 200; selected=True
Result UI HTTP: 200; socket-client=True

psql: select vote, count(*) from votes group by vote order by vote;
a|1
b|1
```

This verifies the complete Vote -> Redis -> Worker -> PostgreSQL -> Result
path, not only HTTP liveness.

