"""Module implements downloading a number of files using asyncio and threads."""

import aiohttp
import asyncio
import os
import requests
import time
from threading import Thread

files_dict = {"50MB": "http://ipv4.download.thinkbroadband.com/50MB.zip",
              "100MB": "http://ipv4.download.thinkbroadband.com/100MB.zip",
              "200MB": "http://ipv4.download.thinkbroadband.com/200MB.zip"}


async def async_download_by_url(session, url_addr):
    async with session.get(url_addr) as response:
        filename = os.path.basename(url_addr)
        with open(filename, 'wb') as f_handle:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f_handle.write(chunk)
        return await response.release()


async def async_download():
    for file_name, url_addr in files_dict.items():
        async with aiohttp.ClientSession() as session:
            await async_download_by_url(session, url_addr)


def sync_download_by_url(url_addr):
    response = requests.get(url)
    filename = "sync_{}".format(os.path.basename(url_addr))
    with open(filename, 'wb') as f_handle:
        for chunk in response.iter_content(1024):
            f_handle.write(chunk)


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_download())
    print("Async download takes {} sec".format(time.time()-start_time))
    start_time = time.time()
    for _, url in files_dict.items():
        thread = Thread(target=sync_download_by_url, args=(url,))
        thread.run()
    print("Thread download takes {} sec".format(time.time() - start_time))
