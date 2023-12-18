# # ##### zadanie 1
num=int(input())
chislo=lambda num: f'{num} четное' if num%2==0 else f'{num} нечетное'
print(chislo(num))

# # ###### zadanie 2
spisok = [1,2,3,4,5,6,7,8,9]
mew_spisok=list(map(lambda x: str(x), spisok))
print(f'список: {spisok}\nчисло имеет тип {type(spisok[1])}\nновый список: {mew_spisok}\nчисла имеют тип{type(mew_spisok[1])}')
#
# # ##### zadanie 3
tup=('qwerty', 'asdfg', 'qwerewq', '1234321', 'ijnmfd', 'omnomonmo')  # 3 shtyki
poly=list(filter(lambda x:  x ==x[::-1] ,tup ))
print(f'палиндромы: {poly}')

# ### zadanie 4
from datetime import datetime

def speed(x):
    def wrapper():
        t_1 = datetime.now()
        x()
        t_2 = datetime.now()
        print(f'скорость программы: {(t_2-t_1).microseconds} микросекунд.')
    return wrapper
@speed
def f():
    for i in range(5):
        i=i**2
        s=[]
        s.append(i)
        print(s,end=' ')
f()
@speed
def f_2():
    count=0
    a=2
    while count!=5:
        count+=1
        a=a**2
    print(a, end=' ')
f_2()
#
# ######## 5    РАБОТАЕТ ТОЛЬКО С ТОЧКОЙ
num = input()
def num_type(num):
    if num.isdigit() == True:
        num = int(num)
        t = f'вы вели целое число = {num}, {type(num)}'
    elif num[:1] == '-' and num[1:].isdigit() == True:
        num = int(num)
        t = f'вы вели целое отрицательне число = {num}, {type(num)}'
    elif num[:1] != '-' and list(map(str.isdigit, num.replace('.', ''))) != True:
        num = float(num)
        t = f'вы ввели положительное число с плавающей точкой = {num}, {type(num)}'
    elif num[:1] == '-' and list(map(str.isdigit, num.replace('.', '1'))) != True:
        num = float(num)
        t = f'вы ввели отрицательное число с плавающей точкой = {num}, {type(num)}'
    else:
        t = f'вы ввели некоректное число = {num}, {type(num)}'
    return t
print(num_type(num))
