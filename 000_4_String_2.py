import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
word = 'Python'
#       012345
print(word[0],word[1],word[2],word[3],word[4],word[5])
print(word[-6],word[-5],word[-4],word[-3],word[-2],word[-1])
print(word[0:2],word[2:5],word[5]) # конец интервала не входит
print(word[:2],word[2:4],word[4:])
print(word[:2]+word[2:4]+word[4:])
print('len(word)=',len(word))
#Строковые переменные не являются изменяемыми
##########################################################
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
print(my_function.__doc__)

##########################################################
#на разбор, сохранил ради сепаратора, сама функция работать не будет
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
