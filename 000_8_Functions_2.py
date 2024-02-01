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
test_text = input(" Для завершения программы нажмите Enter: ")