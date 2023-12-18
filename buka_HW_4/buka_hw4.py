# '''Дана строка в виде случайной последовательности чисел от 0 до 9
# Требуется создать словарь, который в качестве ключей будет
# принимать данные числа (т. е. ключи будут типом int), а в качестве
# значений – количество этих чисел в имеющейся последовательности.
# Вывести на экран словарь из 3-х самых часто встречаемых чисел.'''
#
# from random import randint
#
# count = 0
# spisok = []
# while count != 999:  # kolichestvo ciklov dlya chisel
#     chislo = randint(0, 9)  # random chislo v spisook //// potom v kluchi
#     spisok.append(chislo)
#     # print(spisok)                     ###### del
#     count += 1
#     key = set(spisok)  ## spisok vmnojestvo kluchey
#     dictionary = dict.fromkeys(key, 0)  ####### y kluchey znachenie 0// potom poschitat'
#     # print(dictionary)      ## del
#     for key in spisok:  ### cikl podscheta znacheniya
#         dictionary[key] += 1  ### znachenie +1
# # print(dictionary)            ####  itog slovar' del
# sort_dict = {}  #### nov sortirov. slovar'
# sort_key = sorted(dictionary, key=dictionary.get)[-3::]  #### sortirovka znacheniy ybuvanie
# # i vybor poslednih 3x
# print(sort_key)           ### del
# for i in sort_key:
#     sort_dict[i] = dictionary[i]  ### + v novyi
# print(sort_dict)  #### sortirovannyi slocar'
#
# ############
# ############
#
# '''Дан словарь, поменять местами ключ и значение. Если значения
# повторяются, ключи объединить в список.'''
#
# dict_name = {'Петя': 'Петров', 'Витя': 'Петров',
#              'Коля': 'Иванов', 'Леша': 'Иванов',
#              'Саша': 'Васильев', 'Гриша': 'Васильев'}
# # print(dict_name)                      ###del
# dict_revers = {}
#
# for name, l_name in dict_name.items():
#     # print(dict_revers)                  ####del
#     if l_name not in dict_revers:
#         dict_revers[l_name] = name
#     else:
#         spisok = []
#         spisok.append(dict_revers[l_name])
#         spisok.append(name)
#         dict_revers[l_name] = spisok
# print(dict_revers)
#
# #########
# ##########

'''
Обнаружилось, что имена некоторых владельцев повторяются, потому что у
них несколько кошек. Необходимо оптимизировать хранение данных таким
образом, чтобы для каждого владельца при выводе на печать данные о
всех его животных отображались в одной строке:
Игорь Бероев: Муся, 7; Изольда, 2'''

cats = [('Мартин', 5, 'Алексей', 'Егоров'),
        ('Фродо', 3, 'Анна', 'Самохина'),
        ('Вася', 4, 'Андрей', 'Белов'),
        ('Муся', 7, 'Игорь', 'Бероев'),
        ('Изольда', 2, 'Игорь', 'Бероев'),
        ('Снейп', 1, 'Марина', 'Апраксина'),
        ('Лютик', 4, 'Виталий', 'Соломин'),
        ('Снежок', 3, 'Марина', 'Апраксина'),
        ('Марта', 5, 'Сергей', 'Колесников'),
        ('Буся', 12, 'Алена', 'Федорова'),
        ('Джонни', 10, 'Игорь', 'Андропов'),
        ('Мурзик', 1, 'Даниил', 'Невзоров'),
        ('Барсик', 2, 'Виталий', 'Соломин'),
        ('Рыжик', 7, 'Владимир', 'Медведев'),
        ('Матильда', 8, 'Андрей', 'Белов'),
        ('Гарфилд', 3, 'Александр', 'Березуев')]

dict = {}
for i in cats:
    cat_age = i[0] + ' ' + str(i[1])
    name_lname = i[2] + ' ' + i[3]

    # print(f'cat_age\nname_lname')   ##del
    dict[cat_age] = name_lname
new_dict = {}
for name_lname, cat_age in dict.items():
    if cat_age not in new_dict:
        new_dict[cat_age] = name_lname
    else:
        spisok = []
        spisok.append(new_dict[cat_age])
        spisok.append(name_lname)
        new_dict[cat_age] = spisok
print(new_dict)
