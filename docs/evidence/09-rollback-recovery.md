# Rollback recovery evidence

```text
helm rollback voting-app 2 -n voting-app --wait --timeout 5m
Rollback was a success! Happy Helming!

REVISION  STATUS      DESCRIPTION
1         superseded  Install complete
2         superseded  Upgrade complete
3         superseded  Upgrade complete (controlled bad tag)
4         deployed    Rollback to 2

postgres  Ready  Running  postgres:17.11-alpine3.24
redis     Ready  Running  redis:8.4.7-alpine3.22
result    Ready  Running  ...:e30553c367c3c9cddc4661050ebe234bc20af383
vote      Ready  Running  ...:e30553c367c3c9cddc4661050ebe234bc20af383
worker    Ready  Running  ...:e30553c367c3c9cddc4661050ebe234bc20af383

Post-rollback database verification:
a|1
b|1
```

The rollback restored every application workload to the tested SHA while the
database retained the demonstrated votes.

