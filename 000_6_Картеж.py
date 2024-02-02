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
test_text = input(" Для завершения программы нажмите Enter: ")
