import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
##
#
import json
x=[1, 'simple', 'list']
print(json.dumps(x))
#
os.curdir=os.path.dirname(os.path.realpath(__file__))
my_file = open(os.curdir+"\\"+"BabyFile.txt", "w+")
json.dump(x, my_file)
my_file.close()
os.system("notepad "+os.curdir+"\\"+"BabyFile.txt")
#
os.curdir=os.path.dirname(os.path.realpath(__file__))
my_file = open(os.curdir+"\\"+"BabyFile.txt", "r")
x = json.load(my_file)
print(x)
my_file.close()
#
os.system("del "+os.curdir+"\\"+"BabyFile.txt")
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")