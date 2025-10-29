# CodeMaster - Backend (v0.2)

Versión inicial del backend preparada para FastAPI + Uvicorn.

## Estructura

- `backend/app/main.py` - entrada FastAPI

- `backend/app/api/routes_generate.py` - endpoint `/generate`

- `backend/app/adapters/*` - adaptadores para OpenAI, Qwen, DeepSeek (stubs listos)

## Cómo ejecutar (local)

1. Crear virtualenv y activar
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Establecer variables de entorno (ej: OPENAI_API_KEY)
3. Ejecutar
```bash
uvicorn backend.app.main:app --reload
```
