import pytest
import respx
from backend.app.adapters.deepseek_adapter import DeepSeekAdapter

@pytest.mark.asyncio
async def test_deepseek_adapter_success():
    adapter = DeepSeekAdapter(api_key='test-key')
    async with respx.mock(base_url='https://api.deepseek.ai') as rsps:
        rsps.post('/generate').respond(json={'text':'deepseek ok'}, status_code=200)
        result = await adapter.generate(prompt='hello', model='deepseek-test')
        assert result['success'] is True
        assert 'deepseek' in result['text']
