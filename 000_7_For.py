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
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")