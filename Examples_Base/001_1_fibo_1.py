import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
import fiboMod
print(fiboMod.fib(1000))
print(fiboMod.fib2(100))
##
# dir - интроспекция
print(dir(fiboMod))
import sys
print(dir(sys))
print(dir())
##########################################################

test_text = input(" Для завершения программы нажмите Enter: ")