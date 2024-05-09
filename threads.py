import threading, multiprocessing
from time import time

x = 1000000
n = 2

def main():
    runtime_thread = 0
    for i in range(10):
        runtime_thread += run_threads()
    print(f"Avg thread: {runtime_thread/10}")

    runtime_single = 0
    for i in range(10):
        runtime_single += run_single()
    print(f"Avg single: {runtime_single/10}")

def thread_main(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

def run_threads():
    threads = []
    for i in range(n):
        # threads.append(threading.Thread(target=thread_main, args=[x]))
        threads.append(multiprocessing.Process(target=thread_main, args=[x]))

    time1 = time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    time2 = time()

    # print(f"Running time: {time2 - time1}")
    return time2 - time1

def run_single():
    time1 = time()
    for i in range(n):
        thread_main(x)
    time2 = time()

    # print(f"Running time: {time2 - time1}")
    return time2 - time1

main()