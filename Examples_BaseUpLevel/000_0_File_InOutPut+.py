import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
#Программный код не работает без
# 1) os.curdir по умолчанию пустой, нужно вывернуть его в целевую дирректорий
# 2) пиши полный путь к файлу...
##
# - Открыть на запись или чтение - 
# f = open(file_name, access_mode, encoding="utf-8")
# file_name = имя открываемого файла
# access_mode =
# r	Только для чтения.
# w	Только для записи. Создаст новый файл, если не найдет с указанным именем.
# rb	Только для чтения (бинарный).
# wb	Только для записи (бинарный). Создаст новый файл, если не найдет с указанным именем.
# r+	Для чтения и записи.
# rb+	Для чтения и записи (бинарный).
# w+	Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
# wb+	Для чтения и записи (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
# a	Откроет для добавления нового содержимого. Создаст новый файл для записи, если не найдет с указанным именем.
# a+	Откроет для добавления нового содержимого. Создаст новый файл для чтения записи, если не найдет с указанным именем.
# ab	Откроет для добавления нового содержимого (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
# ab+	Откроет для добавления нового содержимого (бинарный). Создаст новый файл для чтения записи, если не найдет с указанным именем.
##########################################################
# w+	Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
# Предыдущий файл с таким названием удаляется...
os.curdir=os.path.dirname(os.path.realpath(__file__))
print(os.curdir)
my_file = open(os.curdir+"\\"+"BabyFile.txt", "w+")
my_file.write("ALT+F4 - для закрытия блокнота в фокусе на нем и продолжения основной программы\n")
my_file.write("Привет мир!\n")
my_file.write("Пишу в файл с его пересозданием\n")
my_file.close()
print('Открываю файл в блокноте.')
os.system("notepad "+os.curdir+"\\"+"BabyFile.txt")
##
# a+	Дозапись. Откроет для добавления нового содержимого. Создаст новый файл для чтения записи, если не найдет с указанным именем.
os.curdir=os.path.dirname(os.path.realpath(__file__))
print(os.curdir)
my_file = open(os.curdir+"\\"+"BabyFile.txt", "a+")
my_file.write("Дописываю в конец файла\n")
my_file.write("!!!!!!!!!!!!!!!!!!!!!!!\n")
my_file.close()
os.system("notepad "+os.curdir+"\\"+"BabyFile.txt")
##
# -  r	Только для чтения.
os.curdir=os.path.dirname(os.path.realpath(__file__))
print(os.curdir)
print("Чтение из файла 1")
my_file = open(os.curdir+"\\"+"BabyFile.txt", "r")
read_data = my_file.read()
print(read_data)
my_file.close()
##
#
print("Чтение из файла 2")
with open(os.curdir+"\\"+"BabyFile.txt", "r") as my_file:
	read_data = my_file.read()
	print(read_data)
	my_file.close()
##
# - не самый адекватный способ но запомнить нужно
print("Чтение из файла 3")
with open(os.curdir+"\\"+"BabyFile.txt", "r") as my_file:
	print(my_file.readline(), end='')
	print(my_file.readline(), end='')
	print(my_file.readline(), end='')
	print(my_file.readline(), end='')
	print(my_file.readline(), end='')
	my_file.close()
##
# - на сайте говорят что именно этот способ самый кашерный по производительности и экономии памяти...
print("Чтение из файла 4")
with open(os.curdir+"\\"+"BabyFile.txt", "r") as my_file:
	for line in my_file:
		print(line, end='')
	my_file.close()
##
# - my_file.readlines() - получает строки файла массивом
print("Чтение из файла 5")
with open(os.curdir+"\\"+"BabyFile.txt", "r") as my_file:
	for line in my_file.readlines():
		print(line, end='')
	my_file.close()
##
# - list(my_file) - получает строки файла массивом
print("Чтение из файла 6")
with open(os.curdir+"\\"+"BabyFile.txt", "r") as my_file:
	for line in list(my_file):
		print(line, end='')
	my_file.close()

##
#
print('rwerwerwee')
os.system("del "+os.curdir+"\\"+"BabyFile.txt")
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")