import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
from fiboMod import fib, fib2
print(fib(1000))
print(fib2(100))
##########################################################

test_text = input(" Для завершения программы нажмите Enter: ")