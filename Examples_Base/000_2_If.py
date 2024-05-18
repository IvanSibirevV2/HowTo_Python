import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
def Test_1():
	the_world_is_flat = True
	#the_world_is_flat = False
	if the_world_is_flat:
		print("the_world_is_flat = True")
	else :
		print('the_world_is_flat = False')
#Test_1()
##########################################################
def Test_2():
	x = int(input("Please enter an integer: "))
	if x < 0:
		x = 0
		print('Negative changed to zero')
	elif x == 0:
		print('Zero')
	elif x == 1:
		print('Single')
	else:
		print('More')
#Test_2()
#Switch Case Match в питоне толи не существуют толи неработают
#толи реализованы крайне монструозно... Рекомендую if_elsIf_else
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
