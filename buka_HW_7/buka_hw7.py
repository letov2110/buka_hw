from datetime import datetime
# ## zadanie 1
# # n=input() #nachalo
# # m=input()  ## knec
# def work_time(f):
#     def wraper():
#         s_t=datetime.strptime('9:00','%H:%M').time()  #n
#         l_t=datetime.strptime('18:00','%H:%M').time() ##m
#         mow_t=datetime.now().time()
#         if mow_t>=s_t and mow_t<=l_t:
#              return f()
#         else:
#             print('не рабоает')
#     return wraper
# @work_time
# def work():
#     print('работает')
# work()

## zadanie 2
def type_check(correct_type):
    def fun(arg_fun):
        def f(arg):
            if(isinstance(arg, correct_type)):
                return arg_fun(arg)
            else:
                print('bad')
        return f
    return fun

@type_check(int)
def chislo(num):
    return num*2
@type_check(str)
def f_letter(word):
    return word[0]
print('*'*99)
print(chislo(2))
chislo('hi')
print('*'*99)
print(f_letter('hi world'))
f_letter(1.5)
print('*'*99)
