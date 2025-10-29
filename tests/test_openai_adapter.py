import pytest
import respx
import httpx
import asyncio
from backend.app.adapters.openai_adapter import OpenAIAdapter

@pytest.mark.asyncio
async def test_openai_adapter_success(monkeypatch):
    adapter = OpenAIAdapter(api_key='test-key')
    # mock OpenAI responses endpoint
    async with respx.mock(base_url='https://api.openai.com') as rsps:
        rsps.post('/v1/responses').respond(json={'output':[{'content':'hello world'}]}, status_code=200)
        result = await adapter.generate(prompt='hi', model='gpt-test')
        assert result['success'] is True
        assert 'hello world' in result['text']

@pytest.mark.asyncio
async def test_openai_adapter_failure(monkeypatch):
    adapter = OpenAIAdapter(api_key='test-key')
    async with respx.mock(base_url='https://api.openai.com') as rsps:
        rsps.post('/v1/responses').respond(status_code=500)
        result = await adapter.generate(prompt='hi', model='gpt-test')
        assert result['success'] is False
        assert 'error' in result['meta']
