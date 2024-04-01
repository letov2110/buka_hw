import threading

lock = threading.Lock()
even = []
odd = []

def find():
    global even, odd
    for i in range(1, 20):
        if i % 2 == 0:
            with lock:
                even.append(i)
        else:
            with lock:
                odd.append(i)

t1 = threading.Thread(target=find)
t2 = threading.Thread(target=find)

t1.start()
t2.start()
t1.join()
t2.join()

print(f'четные: {even}\nнечетные: {odd}')

#############
import threading

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def find_factorial(n,result):
    result[n] = factorial(n)

if __name__ == "__main__":
    n = int(input('факториал числа: '))
    result = {}
    threads = []

    for i in range(3):
        thread = threading.Thread(target=find_factorial, args=(n,result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"равен {result[n]}")