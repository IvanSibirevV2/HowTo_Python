import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
#используйте коллекции.deque, который был разработан для быстрого добавления
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print("queue=",queue)
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print("queue.popleft()","\n    ",queue.popleft())
print(queue)
print("queue.popleft()","\n    ",queue.popleft())
print(queue)
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")