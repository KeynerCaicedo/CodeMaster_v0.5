import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.app.services.orchestrator import CodeOrchestrator

logger = logging.getLogger(__name__)
router = APIRouter()

# --- Modelo de entrada del endpoint ---
class GenerateRequest(BaseModel):
    prompt: str
    model: str = "gpt-4o-mini"  
    provider: str = "openai"    
    meta: dict | None = None


@router.post("/generate/")
async def generate(request: GenerateRequest):
    """
    Endpoint principal para generación/corrección de código.
    Usa la pipeline del CodeOrchestrator (OpenAI → Qwen → DeepSeek).
    """
    logger.info("Received generate request")

    orchestrator = CodeOrchestrator()

    try:
        # Ejecutar pipeline completa
        final_result = await orchestrator.process(
            prompt=request.prompt,
            model=request.model,
            meta=request.meta or {}
        )

        # Validar éxito
        if not final_result.get("success"):
            raise HTTPException(
                status_code=502,
                detail=final_result.get("error", "Error desconocido en la pipeline")
            )

        logger.info("Pipeline ejecutada correctamente.")
        return {
            "status": "success",
            "message": "Pipeline completada con éxito",
            "data": final_result
        }

    except HTTPException as e:
        raise e  # Repropagar errores HTTP conocidos

    except Exception as e:
        logger.error("Unhandled error in generate endpoint", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error interno del servidor: {str(e)}"
        )
