import asyncio
import logging
from .base_adapter import AdapterResult

logger = logging.getLogger(__name__)

class MockAdapter:
    """Simula las respuestas de los modelos para pruebas sin conexión ni créditos."""

    async def generate(self, prompt: str, model: str = "mock-model", meta: dict = None):
        logger.info(f"[MOCK] Recibido prompt para modelo {model}: {prompt[:50]}...")
        await asyncio.sleep(1)  # simula tiempo de respuesta

        # Genera un texto simulado distinto según el "modelo"
        if "openai" in model.lower():
            response = f"[OPENAI MOCK OUTPUT] Código base generado para: {prompt[:40]}..."
        elif "qwen" in model.lower():
            response = f"[QWEN MOCK OUTPUT] Código refinado: {prompt[:40]}..."
        elif "deepseek" in model.lower():
            response = f"[DEEPSEEK MOCK OUTPUT] Código optimizado y documentado: {prompt[:40]}..."
        else:
            response = f"[GENERIC MOCK OUTPUT] Respuesta generada para {model}"

        return {"result": response, "meta": {"mock": True}}
