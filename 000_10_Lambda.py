import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = [x**2 for x in range(10)]
print(squares)
##########################################################
_vec = [-4, -2, 0, 2, 4]
print("_vec = [-4, -2, 0, 2, 4]","\n    ",_vec)
print("[x*2 for x in _vec]","\n    ",[x*2 for x in _vec])
print("[x for x in _vec if x >= 0]","\n    ",[x for x in _vec if x >= 0])
print("[abs(x) for x in _vec]","\n    ",[abs(x) for x in _vec])
##########################################################
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print("freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']")
print("    ",['  banana', '  loganberry ', 'passion fruit  '])
#"Привет мир".strip()- Глублкое копирование строки чтоли 
print("\"Привет мир\".strip()","\n    ","Привет мир".strip())
##########################################################
# create a list of 2-tuples like (number, square)
print("[(x, x**2) for x in range(6)]","\n    ",[(x, x**2) for x in range(6)])
##########################################################
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print("vec = [[1,2,3], [4,5,6], [7,8,9]]","\n    ",vec)
print("!!!![num for elem in vec for num in elem]","\n    ",[num for elem in vec for num in elem])
##########################################################
from math import pi
print("[str(round(pi, i)) for i in range(1, 6)]","\n    ",[str(round(pi, i)) for i in range(1, 6)])
##########################################################
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print("matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]","\n    ",matrix)
print("[[row[i] for row in matrix] for i in range(4)]","\n    ",[[row[i] for row in matrix] for i in range(4)])
##########################################################
##########################################################
##########################################################
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")