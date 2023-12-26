import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
print ("Путь к текущей дирректории:",os.path.abspath(os.curdir))
print ("Путь к исполняемому файлу:", os.path.dirname(os.path.realpath(__file__)))
print ("Привет Мирр")
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
