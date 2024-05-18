import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
print('spam eggs', "Paris rabbit got your back :)! Yay!") # текст в одинаных кавычках# текст в двойных кавычках
print('spam\'egg\'s','\n \\Однако')# экранирующий спец символ
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print(3 * 'un' + 'ium', 'Py' 'thon')
print(
'Put several strings within parentheses '
'to have them joined together.'
)
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
