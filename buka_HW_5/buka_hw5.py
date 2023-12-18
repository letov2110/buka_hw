# #### zadanie 1
# n = int(input('введите число, чтобы посчитать его факториал:  '))
# def fact(n):
#     if n > 0:
#         return n * fact(n - 1)
#     elif n == 0 or n == 1:
#         return 1
#     elif n < 0:
#         return 'факториал отрицательного числа не определен'
# print(f'\n {n}! = {fact(n)}')


###### zadanie 2
from datetime import datetime
import time
n = int(input('какое коллмчество дат вывести: '))
spisok = []
def d_t():
    q = (datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
    return q
for i in range(n):
    spisok.append(d_t())
    print(spisok)