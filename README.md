# e2e-p-11051145-2

auto run 2

Владелец: group:default/platform

## Разработка
```
pip install -r requirements-dev.txt
ruff check .
pytest
uvicorn app.main:app --app-dir src --port 8080   # http://localhost:8080/health
```

CI (`.github/workflows/ci.yaml`) собирает образ в GHCR и обновляет тег в GitOps-репозитории; деплой выполняет Argo CD.
