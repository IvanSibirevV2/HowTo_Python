import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
the_world_is_flat = True
##the_world_is_flat = False
if the_world_is_flat:
	print("the_world_is_flat = True")
else :
	print('the_world_is_flat = False')
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
