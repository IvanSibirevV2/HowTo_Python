import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
#4.8.2. Keyword Arguments
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")