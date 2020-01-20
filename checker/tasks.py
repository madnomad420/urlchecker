import asyncio
import httpx


async def check_url(url):
    client = httpx.AsyncClient()
    response = await client.get(url.url)
    return { 'id': url.pk, 'status': response.status_code }

async def check_urls(urls):
    coroutines = [check_url(url) for url in urls]
    res = await asyncio.gather(*coroutines)
    return res
