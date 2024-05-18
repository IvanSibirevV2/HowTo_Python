import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
print ("Путь к текущей дирректории:",os.path.abspath(os.curdir))
print ("Путь к исполняемому файлу:", os.path.dirname(os.path.realpath(__file__)))
print ("Привет Мирр")
##
#
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
##
#
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
