# Learn Numpy
import numpy as np
from time import time 
import matplotlib as mat

def funcNumpy(n):
    arr = np.array([range(n)])
    # arr += 10

def funcList(n):
    lst = list(range(n))
    for i in range(n): lst.append(i)
    # for i in range(len(lst)): lst[i] ++ 10

def measure_min_time(fn, *args):
    '''Takes a function with its arguments, runs it 5 times. Returns the fastest running time in seconds.
    Throws an error if fn(*args) throws an error.'''
    min_time = float('inf')
    for i in range(5):
        start = time()
        fn(*args)
        duration = time() - start
        min_time = min(duration, min_time) 
    
    return min_time


if __name__ == '__main__':
    funcNumpy(100)
    print(f" \n\n {'''Functions' Running Times (ms) by Input Size''' : ^50} \n")
    print(f" {'n':>10} {'Numpy': >13} {'List':>15} ")

    for n in [10, 100, 1000, 10**5, 10**6, 10**7]:
        print(f" {n:>10}  {'':>2} {measure_min_time(funcNumpy, n):>6.3e} {''*2:>6}{measure_min_time(funcList, n):>6.3e}")
    print()