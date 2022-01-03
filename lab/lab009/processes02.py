import multiprocessing as mp
import os
import time
import functools

def fibon(n):
    if n < 2:
        return n
    return fibon(n - 1) + fibon(n - 2)

def worker(n):
    fib = fibon(n)
    print(f'Calc: {n} -> {fib}')
    return fib

if __name__ == '__main__':

    start = time.time()
    p = mp.Process(target = worker, args = (43,))
    p.start()
    p.join()
    end = time.time()
    print(f'{end - start = }')