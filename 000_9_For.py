import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
#for
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
##########################################################
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
#list
for i in range(5):
    print(i)
# while - подсмотреть
##
#Цикл по словарю
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
##
#Цикл по массиву
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
for q, a in zip(['name', 'quest', 'favorite color'], ['lancelot', 'the holy grail', 'blue']):
    print('What is your {0}?  It is {1}.'.format(q, a))
##
#Использование set() для последовательности устраняет повторяющиеся элементы.
for f in sorted(set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])):
    print(f)
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")