from fastapi import FastAPI
from backend.app.api.routes_generate import router as generate_router
from backend.app.core.logger import get_logger
from dotenv import load_dotenv
import os
import backend.app.config 
from fastapi import FastAPI
from backend.app.api.routes_generate import router as generate_router


load_dotenv()


app = FastAPI()
app.include_router(generate_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Backend activo y .env cargado correctamente"}

logger = get_logger(__name__)

def create_app() -> FastAPI:
    app = FastAPI(title='CodeMaster Backend', version='0.2')
    app.include_router(generate_router)
    @app.on_event('startup')
    async def startup_event():
        logger.info('Starting CodeMaster Backend')
    return app

app = create_app()
