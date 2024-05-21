import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
try:
  x = int(input("Please enter a number: "))
except ValueError:
  print("Oops!  That was no valid number.  Try again...")

##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")