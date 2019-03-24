"""Module implements downloading a number of files using asyncio and
threads."""

import aiohttp
import asyncio
import requests
import threading
import time


files_dict = {"50MB": "http://ipv4.download.thinkbroadband.com/50MB.zip",
              "100MB": "http://ipv4.download.thinkbroadband.com/100MB.zip",
              "200MB": "http://ipv4.download.thinkbroadband.com/200MB.zip"}


async def async_download_by_url(session, url_addr, file_name):
    async with session.get(url_addr) as response:
        filename = "async_{}".format(file_name)
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
            await async_download_by_url(session, url_addr, file_name)


def thread_download(file_name, url_addr):
    response = requests.get(url_addr)
    filename = "sync_{}".format(file_name)
    with open(filename, 'wb') as f_handle:
        for chunk in response.iter_content(1024):
            f_handle.write(chunk)


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_download())
    print("Async download takes {} sec".format(time.time() - start_time))
    start_time = time.time()
    threads = []
    for file_name, url_addr in files_dict.items():
        threads.append(threading.Thread(target=thread_download,
                                        args=(file_name, url_addr)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Thread download takes {} sec".format(time.time() - start_time))
