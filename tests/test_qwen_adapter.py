import pytest
import respx
from backend.app.adapters.qwen_adapter import QwenAdapter

@pytest.mark.asyncio
async def test_qwen_adapter_success():
    adapter = QwenAdapter(api_key='test-key')
    async with respx.mock(base_url='https://api.qwen.ai') as rsps:
        rsps.post('/generate').respond(json={'text':'qwen says hi'}, status_code=200)
        result = await adapter.generate(prompt='hello', model='qwen-test')
        assert result['success'] is True
        assert 'qwen' in result['text']
