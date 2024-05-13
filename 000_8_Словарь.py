import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
##
#Словарь
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)
##
#Конструктор dict() создает словари непосредственно из последовательностей пар ключ-значение:
p = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(p)
print({x: x**2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
