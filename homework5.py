import asyncio, aiohttp
import async_timeout


async def download_file(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def main(url):
    async with aiohttp.ClientSession() as session:
        response_text = await download_file(session, url)
        print(response_text)

loop = asyncio.get_event_loop()
print(loop.is_running())
loop.run_until_complete(main("https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz"))
