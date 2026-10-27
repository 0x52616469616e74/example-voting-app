# Local Compose health evidence

Captured on 2026-10-27 at approximately 19:43 WAT from the repository root:

```bash
docker compose ps
```

| Service | State | Health | Published port |
| --- | --- | --- | --- |
| `vote` | Running | Healthy | `8080` |
| `result` | Running | Healthy | `8081` |
| `worker` | Running | Application process active | None |
| `redis` | Running | Healthy | Internal only |
| `db` | Running | Healthy | Internal only |

The browser test selected Dogs on the Vote page. The Result page then showed
Dogs at 100%, demonstrating the Vote -> Redis -> Worker -> PostgreSQL -> Result
flow. See [`02a-vote-page.png`](02a-vote-page.png) and
[`02b-result-page.png`](02b-result-page.png).
