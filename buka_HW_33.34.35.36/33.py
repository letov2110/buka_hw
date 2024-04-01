import threading

def plus_one(num):
    num += 1
    print(f"thread {i+1} : {num}")

num = 2
threads = []
for i in range(3):
    thread = threading.Thread(target=plus_one, args=(num,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
##########

import multiprocessing

def plus_one(num):
    num += 1
    print(f"procss {i+1}: {num}")

num = 2
processes = []
for i in range(3):
    process = multiprocessing.Process(target=plus_one, args=(num,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()