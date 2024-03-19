# 0x02. Python - Async Comprehension
## Learning Objectives
1) How to write an asynchronous generator
2) How to use async comprehensions
3) How to type-annotate generators

## Learning
Asynchronous generators allow you to produce a sequence of values asynchronously. Asynchronous generators can be used with asyncio.gather to manage multiple asynchronous generators concurrently. Here is how to write and asynchronous generator using ```async def````
and ```yield``` keywords.
**Example:
```
from typing import AsyncGenerator
async def generate_numbers(n: int) -> AsyncGenerator[int]:
  """
  Asynchronously generates numbers from 1 to n.
  """
  for i in range(1, n + 1):
    await asyncio.sleep(1)  # Simulate some asynchronous operation
    yield i

async def main():
  async for num in generate_numbers(5):
    print(num)

asyncio.run(main())  # Output: 1 (after 1 sec) 2 (after 1 sec) ... 5 (after 1 sec) 
```
generate_numbers is an asynchronous generator function. It uses a loop that iterates from 1 to n. Inside the loop, await asyncio.sleep(1) simulates an asynchronous operation that takes 1 second. The yield i statement suspends the generator function and returns the value i to the caller. When the caller resumes the generator (in the loop of main) the function continues from where it yielded. 

Async comprehensions provide a compact way to write asynchronous iterators. They are efficient because they avoid repeated calls to await and unnecessary creation of intermediate lists. Here is a basic example:
```
async def fetch_data(url):
  # Simulate fetching data from a URL
  await asyncio.sleep(1)  # Simulate asynchronous operation
  return f"Data from {url}"

async def main():
  urls = ["https://example.com/1", "https://example.com/2", "https://example.com/3"]
  data = [await fetch_data(url) for url in urls]  # Async comprehension
  for item in data:
    print(item)

asyncio.run(main())  # Output: Data from https://example.com/1 ... (after 1 sec)
```
The example follows the syntax:
```
async_iterator = [async expression for target in async_iterable if condition]
```

## Requirements
1) Allowed editors: vi, vim, emacs
2) All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
3) All your files should end with a new line
4) The first line of all your files should be exactly #!/usr/bin/env python3
5) A README.md file, at the root of the folder of the project, is mandatory
6) Your code should use the pycodestyle style (version 2.5.x)
7) The length of your files will be tested using wc
8) All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
9) All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
10) A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
11) All your functions and coroutines must be type-annotated.


## Tasks
### 0. Async Generator
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

### 1. Async Comprehensions
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async which comprehends over async_generator, then return the 10 random numbers.

### 2. Run time for four parallel comprehensions
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
