import os
import logging
from typing import Dict, Any
from openai import OpenAI, RateLimitError, APIConnectionError, APIError
from dotenv import load_dotenv
from .base_adapter import AdapterResult

# --- Configuración de logging ---
logger = logging.getLogger(__name__)

# --- Cargar variables de entorno ---
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.env"))
load_dotenv(dotenv_path)
print(".env cargado desde:", dotenv_path)
print("OPENAI_API_KEY detectado:", os.getenv("OPENAI_API_KEY"))

# --- Cargar el prompt del sistema ---
PROMPT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../prompts/openai_prompt.md"))
try:
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        SYSTEM_PROMPT = f.read().strip()
    print(f"Prompt de OpenAI cargado desde: {PROMPT_PATH}")
except FileNotFoundError:
    SYSTEM_PROMPT = "Eres un asistente experto y profesional en programación. Usa código limpio, eficiente y bien documentado."
    print(f"No se encontró el archivo de prompt en {PROMPT_PATH}. Usando prompt por defecto.")

class OpenAIAdapter:
    """Adaptador asíncrono para OpenAI."""
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("No se encontró OPENAI_API_KEY en el entorno o en .env")
        self.client = OpenAI(api_key=self.api_key)

    async def generate(self, prompt: str, model: str = "gpt-4o-mini", meta: Dict[str, Any] = None):
        """
        Envía una solicitud de generación de código o corrección a OpenAI.
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ]
            )
            return {"result": response.choices[0].message.content}

        except RateLimitError:
            logger.error("Error de cuota: cuenta sin créditos disponibles o límite alcanzado.")
            return {"error": "Créditos insuficientes o límite de uso alcanzado. Revisa tu plan en OpenAI."}

        except APIConnectionError:
            logger.error("Error de conexión con los servidores de OpenAI.")
            return {"error": "No se pudo conectar con los servidores de OpenAI. Intenta nuevamente más tarde."}

        except APIError as e:
            logger.error(f"Error general de OpenAI: {str(e)}")
            return {"error": f"Error interno del servicio OpenAI: {str(e)}"}

        except Exception as e:
            import traceback
            error_trace = traceback.format_exc()
            logger.error(f"Error inesperado en OpenAIAdapter.generate(): {str(e)}")
            print("ERROR EN OpenAIAdapter.generate():")
            print(error_trace)
            return {
                "success": False,
                "text": "",
                "meta": {"error": str(e), "trace": error_trace},
            }
