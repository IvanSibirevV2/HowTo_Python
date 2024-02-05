import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = [x**2 for x in range(10)]
print(squares)
##########################################################
##########################################################

test_text = input(" Для завершения программы нажмите Enter: ")