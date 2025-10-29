import logging
from backend.app.adapters.qwen_adapter import QwenAdapter
from backend.app.adapters.deepseek_adapter import DeepSeekAdapter
from backend.app.adapters.openai_adapter import OpenAIAdapter
from backend.app.services.model_router import ModelRouter

logger = logging.getLogger(__name__)

class CodeOrchestrator:
    """
    Orquestador de modelos que combina OpenAI, Qwen y DeepSeek
    para generar, validar y optimizar código de manera colaborativa.
    """

    def __init__(self):
        self.openai = OpenAIAdapter()
        self.qwen = QwenAdapter()
        self.deepseek = DeepSeekAdapter()

    async def process(self, prompt: str, model: str = None, provider: str = "openai", meta: dict = None):

        """
        Ejecuta la pipeline completa:
        1. OpenAI genera o reescribe código base.
        2. Qwen valida y corrige errores.
        3. DeepSeek optimiza rendimiento y estilo final.
        """
        try:
            logger.info("Iniciando pipeline de generación de código...")

            # --- Paso 1: Generación base (OpenAI) ---
            logger.info("➡️  [OpenAI] Generando código base...")
            step1 = await self.openai.generate(prompt, model="gpt-4o-mini", meta=meta)
            if "error" in step1:
                return {"error": f"OpenAI falló: {step1['error']}"}

            base_code = step1["result"]

            # --- Paso 2: Validación técnica (Qwen) ---
            logger.info("➡️  [Qwen] Validando y corrigiendo el código...")
            step2_prompt = f"Valida, depura y mejora el siguiente código, sin alterar su propósito:\n\n{base_code}"
            step2 = await self.qwen.generate(step2_prompt, model="qwen/qwen-2.5-7b-instruct", meta=meta)
            if "error" in step2:
                return {"error": f"Qwen falló: {step2['error']}"}

            validated_code = step2["result"]

            # --- Paso 3: Optimización avanzada (DeepSeek) ---
            logger.info("➡️  [DeepSeek] Optimizando eficiencia y rendimiento...")
            step3_prompt = (
                f"Optimiza el siguiente código para máximo rendimiento, legibilidad y escalabilidad.\n"
                f"Aplica buenas prácticas y documenta brevemente si es necesario:\n\n{validated_code}"
            )
            step3 = await self.deepseek.generate(step3_prompt, model="deepseek-chat", meta=meta)
            if "error" in step3:
                return {"error": f"DeepSeek falló: {step3['error']}"}

            optimized_code = step3["result"]

            logger.info("Pipeline completada exitosamente.")
            return {
                "success": True,
                "steps": {
                    "openai_output": base_code,
                    "qwen_output": validated_code,
                    "deepseek_output": optimized_code
                },
                "final_result": optimized_code
            }

        except Exception as e:
            import traceback
            error_trace = traceback.format_exc()
            logger.error(f"Error en CodeOrchestrator.process(): {str(e)}")
            print("ERROR EN CodeOrchestrator.process():")
            print(error_trace)
            return {
                "success": False,
                "error": str(e),
                "trace": error_trace
            }
