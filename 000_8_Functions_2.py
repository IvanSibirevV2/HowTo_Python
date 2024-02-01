import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
print('--000--')
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(0))
print(f(1))
##########################################################
#рефлексивное описание параметров функции
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
f('spam')
##########################################################

test_text = input(" Для завершения программы нажмите Enter: ")