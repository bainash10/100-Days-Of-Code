#doing asynchronous processes in python to utilize time,
#it is neither multithreading or multiprocessing, it is only a method to use program concurrently,
#pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner.

import time
import asyncio
import requests


async def function1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram1.ico", "wb").write(response.content)
    print("func1")
    return "Nischal"

async def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.ico", "wb").write(response.content)
    print("func2")

async def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
    print("func3")

async def main():
    # task= asyncio.create_task(function1())
    L = await asyncio.gather( #this will download files concurrently
        function1(),
        function2(),
        function3(),
        )
    print(L)


asyncio.run(main())