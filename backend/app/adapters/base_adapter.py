from typing import Protocol, Dict, Any

class AdapterResult(Dict):
    """Estructura estándar de salida de un adaptador."""
    pass

class BaseAdapter(Protocol):
    async def generate(self, prompt: str, model: str, meta: Dict[str, Any] = None) -> AdapterResult:
        """Genera texto a partir de un prompt usando un modelo concreto.
        Documentación ligera en español.
        """
        ...
