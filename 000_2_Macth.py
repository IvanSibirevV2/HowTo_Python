import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
#os.system("start https://docs.python.org/3/tutorial/introduction.html")
#https://docs.python.org/3/tutorial/introduction.html
var=2 + 2
print (var)
print(50 - 5*6)
print('>>>>>>>>>>>>>>>')
print((50 - 5*6) / 4)
print(17 / 3 )
print(17 // 3 )
print(17 % 3)
print(5 ** 2)
print(2 ** 7)
width = 20
height = 5 * 9
print(width * height)
##########################################################
double = 12.5 / 100
print(round(double, 2))
print(round(double, 3))
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
