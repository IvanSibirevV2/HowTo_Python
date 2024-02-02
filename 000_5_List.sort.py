import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
a = [0,1, 2, 3, 4, 5]
print("a = [0,1, 2, 3, 4, 5]","\n    ",a)
a.sort()
print("a.sort()","\n    ",a)
a.sort(reverse=True)
print("a.sort(reverse=True)","\n    ",a)
a = [0,1, 2, 3, 4, 5]
print("a = [0,1, 2, 3, 4, 5]","\n    ",a)
a.reverse()
print("a.reverse()","\n    ",a)
"""

list.copy()
Возвращает неглубокую копию списка. Эквивалентно [:].

Пример, в котором используется большинство методов списка:
"""
##########################################################
#https://pythonim.ru/list/metod-sort-python
def custom_key(people):return people[1]
persons = [['Alice', 26, 'F'], ['Trudy', 25, 'M'], ['Bob', 25, 'M'], ['Alexa', 22, 'F']]
print(persons)
persons.sort(key=custom_key)
print(persons,"\n")
##########################################################
import functools
def compare_function(person_a, person_b):
	if person_a[2] == person_b[2]:
	# if their gender become same
		return person_a[1] - person_b[1]
		# return True if person_a is younger 
	else: 
	# if their gender not matched 
		if person_b[2] == 'F':
	# give person_b first priority if she is female 
			return 1 
		else: # otherwise give person_a first priority 
			return -1
persons = [['Alice', 26, 'F'], ['Trudy', 25, 'M'], ['Bob', 24, 'M'], ['Alexa', 22, 'F']]
print(persons)
print("Before sorting:",persons)
persons.sort(key=functools.cmp_to_key(compare_function))
print("After sorting:",persons)
##########################################################
#https://pythonim.ru/list/metod-sort-python
#При желании можно продолжить
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")