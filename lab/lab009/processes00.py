import multiprocessing as mp
import os
import time
import functools
from concurrent.futures import ProcessPoolExecutor

def fibon(n):
    if n < 2:
        return n
    return fibon(n - 1) + fibon(n - 2)

def worker(n):
    fib = fibon(n)
    print(f'Calc: {n} -> {fib}')
    return fib

start = time.time()
for n in range(41):
    worker(n)
stop = time.time()
print(f'{stop - start = }')