import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
##
#
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
##
#
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
##
# repr - вроде как используется для конвертации в строку и вывода на экран  текствого представления объектов
s = 'Hello, Geeks.'
print (repr(s))
print (repr(2.0/11.0))
##
#class str(object='')¶
#class str(object=b'', encoding='utf-8', errors='strict')
#Ну вы поняли
print(str(b'Zoot!'))
print(repr((32.5, 40000, ('spam', 'eggs'))))
##
#
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
##
#
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
##
#
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
##
#
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
##
# - Коротко о том как обрезать, проверьте сами
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
#str.ljust()
#str.center()
#(Если вы действительно хотите выполнить усечение, вы всегда можете добавить операцию среза, как в x.ljust(n)[:n].)

##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
