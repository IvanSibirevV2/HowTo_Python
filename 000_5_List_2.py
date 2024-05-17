import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
##########################################################
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

for i in range(5):
    print(i)
##########################################################
#Диапазон от 5 до 10 предположительно с шагом в 1
print(list(range(5, 10)))
##########################################################
#Диапазон от 0 до 10 предположительно с шагом в 2
print(list(range(0, 10, 2)))
##########################################################
#Ну вы поняли
print(list(range(-10, -100, -30)))
##########################################################
#
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])
##########################################################
#Удаление элемента массива
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)
##
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[2:4]
print(a)
##
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[:]
print(a)
##
#Удалить переменную
del a
##########################################################
#На разбор
list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]


##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")