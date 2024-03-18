# 0x01. Python - Async
## Learning Objectives
1) async and await syntax
2) How to execute an async program with asyncio
3) How to run concurrent coroutines
4) How to create asyncio tasks
5) How to use the random module

## Learning
Async and await are the foundation of asynchronicity in python. Asynchronous programming simply allows multiple tasks to run concurrently without blocking the main program. 
```
async def
```
The async def keyword defines an asynchronous function, also known as a coroutine. A coroutine can be suspended and resumed later while it waits for I/O operations to complete.

```
await
```
The await expression is used within an async def function to pause execution until a specific awaitable object becomes available. When await is encountered, the event loop takes over, allowing other coroutines to run while the awaited operation is pending.

**Example:
```
import asyncio

async def download_file(url):
    # Simulate downloading a file
    await asyncio.sleep(2)  # Simulate waiting for download
    return f"Downloaded {url}"

async def main():
    urls = ["https://file1.com", "https://file2.com", "https://file3.com"]
    tasks = [download_file(url) for url in urls]
    results = await asyncio.gather(*tasks)  # Run coroutines concurrently
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
```
**Example usage of asyncio:
```
import asyncio

async def wait_and_print(message, delay):
    await asyncio.sleep(delay)  # Simulate some waiting time
    print(message)

async def main():
    # Create an asyncio task for wait_and_print
    task = asyncio.create_task(wait_and_print("Hello from the task!", 2))

    # Execute some code concurrently with the task
    print("Doing something else while the task waits...")
    await asyncio.sleep(1)  # Simulate doing some work

    # Wait for the task to finish (optional)
    # await task  # Uncomment to wait for the task to complete before continuing

    print("Task finished!")

if __name__ == "__main__":
    asyncio.run(main())
```

## Requirements
1) A readme file at the root of the folder of the project, is mandatory
2) Allowed editors: vi, vim, emacs
3) All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3
4) All your files should end with a new line
5) All your files must be executable
6) The length of your files will be tested using wc
7) The first line of all your files should be exactly #!/usr/bin/env python3
8) Your code should use the pycodestyle style
9) All your functions and coroutines must be type-annotated
10) All your modules should have a documentation
11) All your functions should have a documentation
12) A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks
### 0. The basics of async
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
Use the random module.

### 1. Let's execute multiple coroutines at the same time with async
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.

### 2. Measure the runtime
From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time.

### 3. Tasks
Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns an asyncio.Task.

### 4. Tasks
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.

