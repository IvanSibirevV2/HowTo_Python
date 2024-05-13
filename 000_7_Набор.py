import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
##
#Наборы
basket = set()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
print('orange' in basket)
print('crabgrass' in basket)
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
##
# unique letters in a
print(a)
# letters in a but not in b
print(a - b)
# letters in a or b or both
print(a | b)
# letters in both a and b
print(a & b)
# letters in a or b but not both
print(a ^ b)
##
print({x for x in 'abracadabra' if x not in 'abc'})
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
