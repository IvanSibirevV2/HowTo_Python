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
test_text = input(" Для завершения программы нажмите Enter: ")