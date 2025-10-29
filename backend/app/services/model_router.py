from typing import Dict
from backend.app.adapters.openai_adapter import OpenAIAdapter
from backend.app.adapters.qwen_adapter import QwenAdapter
from backend.app.adapters.deepseek_adapter import DeepSeekAdapter

class ModelRouter:
    """Router simple que devuelve el adaptador apropiado por provider key (openai/qwen/deepseek)."""
    def __init__(self):
        self.adapters: Dict[str, object] = {
            'openai': OpenAIAdapter(),
            'qwen': QwenAdapter(),
            'deepseek': DeepSeekAdapter(),
        }

    def route(self, provider: str):
        key = (provider or '').lower()
        if key not in self.adapters:
            raise ValueError(f"Provider not supported: {provider}")
        return self.adapters[key]
