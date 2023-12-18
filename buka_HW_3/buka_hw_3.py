# zadanie 1
stroka = input("введи 2 слова ").split()
word_1 = stroka[0]
word_2 = stroka[1]
word_1, word_2 = word_2, word_1
print('!{} ! {}!'.format(word_1, word_2))
print('!%s ! %s!' % (word_1, word_2))
print(f'!{word_1} ! {word_2}!')

# zadanie 2 i zadanie 3
count = 1
while count > 0:
    name = input("имя: ").capitalize()
    age = int(input("возраст: "))
    count += 1
    if age <= 0:
        print('Ошибка, повторите ввод')
    elif 0 < age < 10:
        print(f'Привет, шкет {name}')
    elif 10 <= age <= 18:
        print(f'Как жизнь {name}?')
    elif 18 < age < 100:
        print(f'Что желаете {name}?')
    else:
        print(f'{name}, вы лжете - в наше время столько не живут..')

# zadanie 4
#########   for
num = int(input('число: '))
summa = 0
for i in range(1, num + 1):
    summa += i ** 3
print(f'сумма кубов = {summa}')
#########   while
num = int(input('число: '))
summa = 0
i = 0
while i != num:
    i += 1
    summa += i ** 3
print(f'сумма кубов = {summa}')
