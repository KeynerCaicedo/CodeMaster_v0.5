import os
import logging
from typing import Dict, Any
import httpx
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from .base_adapter import AdapterResult
from dotenv import load_dotenv

# --- Configuración de logging ---
logger = logging.getLogger(__name__)

# --- Cargar variables de entorno ---
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.env"))
load_dotenv(dotenv_path)
print(".env cargado desde:", dotenv_path)
print("QWEN_API_KEY detectado:", os.getenv("QWEN_API_KEY"))

# --- Variables de entorno de Qwen ---
QWEN_API_KEY = os.getenv('QWEN_API_KEY')
QWEN_BASE_URL = os.getenv('QWEN_BASE_URL', 'https://api.qwen.ai')
QWEN_TIMEOUT = int(os.getenv('QWEN_TIMEOUT', '30'))

# --- Cargar prompt del sistema ---
PROMPT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../prompts/qwen_prompt.md"))
try:
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        SYSTEM_PROMPT = f.read().strip()
    print(f"Prompt de Qwen cargado desde: {PROMPT_PATH}")
except FileNotFoundError:
    SYSTEM_PROMPT = (
        "Eres un asistente experto en análisis y revisión de código. "
        "Tu tarea es validar, analizar y sugerir mejoras con precisión técnica, "
        "manteniendo estándares de calidad y consistencia en los resultados."
    )
    print(f"No se encontró el archivo de prompt en {PROMPT_PATH}. Usando prompt por defecto.")


class QwenAdapter:
    """Adaptador para Qwen (stub). Maneja comunicación asíncrona con la API de Qwen."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or QWEN_API_KEY
        self.base_url = QWEN_BASE_URL
        if not self.api_key:
            raise ValueError("No se encontró QWEN_API_KEY en el entorno o en .env")

    @retry(
        wait=wait_exponential(multiplier=1, min=2, max=10),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(httpx.HTTPError),
    )
    async def _post(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        headers = {'Authorization': f'Bearer {self.api_key}'} if self.api_key else {}
        async with httpx.AsyncClient(timeout=QWEN_TIMEOUT) as client:
            r = await client.post(f"{self.base_url}{path}", json=payload, headers=headers)
            r.raise_for_status()
            return r.json()

    async def generate(self, prompt: str, model: str = "qwen/qwen-2.5-7b-instruct", meta: dict = None):
        """
        Envía una solicitud a la API de Qwen para generar o corregir código.
        """
        try:
            payload = {
                "model": model,
                "input": [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            result = await self._post("/v1/chat/completions", payload)
            return {"result": result.get("output", "Sin respuesta del modelo Qwen.")}

        except httpx.RequestError as e:
            logger.error(f"Error de conexión con los servidores de Qwen: {str(e)}")
            return {"error": "No se pudo conectar con los servidores de Qwen. Intenta nuevamente más tarde."}

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                logger.error("Error de cuota: créditos insuficientes o límite alcanzado (Qwen).")
                return {"error": "Créditos insuficientes o límite de uso alcanzado en Qwen. Revisa tu plan o API key."}
            else:
                logger.error(f"Error HTTP desde Qwen: {e.response.text}")
                return {"error": f"Error HTTP desde Qwen: {e.response.text}"}

        except Exception as e:
            import traceback
            error_trace = traceback.format_exc()
            logger.error(f"Error inesperado en QwenAdapter.generate(): {str(e)}")
            print("ERROR EN QwenAdapter.generate():")
            print(error_trace)
            return {
                "success": False,
                "text": "",
                "meta": {"error": str(e), "trace": error_trace},
            }
