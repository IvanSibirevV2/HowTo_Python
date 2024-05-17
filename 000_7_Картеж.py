import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
#Обратите внимание, очень похоже на кортеж
a, b = 0, 1
while a < 10:
    print(a,b)
    a, b = b, a+b
##########################################################
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
##
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
##
# Tuples are immutable: -  работать не будет
# t[0] = 88888
##
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
##
#Созданеи кортежа единичной мощьности (из одного элемента)
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)
##
#Упаковка\распаковка картежа
t = 12345, 54321, 'hello!'
x, y, z = t
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
