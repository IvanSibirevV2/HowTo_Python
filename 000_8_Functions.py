import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
print('--000--')
def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()
# Now call the function we just defined:
fib(2000)
print(fib)
##########################################################
print('--001--')
def fib2(n):  # return Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)    # see below
		a, b = b, a+b
	return result
f100 = fib2(100)    # call it
print(f100)
#4.8.1. Default Argument Values¶
##########################################################
print('--002--')
#сначала заданны просто параметры
#потом заданы параметры по умолчанию
def fib3(var1,var2=1,var3='212'):  
	print('var1=',var1)
	print('var2=',var2)
	print('var3=',var3)
fib3('Привет мир')
fib3('Привет мир',var2=None)
##########################################################
print('--003--')
i = 5
def f(arg=i):
    print(arg)
i = 6
f()
##########################################################
#Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:
print('--004--')
def f(a, L=[]):
	L.append(a)
	return L
print(f(1))
print(f(2))
print(f(3))
##########################################################
print('--005--')
#If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L
print(f(1))
print(f(2))
print(f(3))
##########################################################
#_var1, - одна или несколько переменных
#*_argS, - массив
#**_KeyWordS - словарь
def foo(_var1,*_argS, **_KeyWordS):
    print("foo>>")
    print("_var1=", _var1)
    print("_argS=",_argS)
    print("_KeyWordS=",_KeyWordS)
    print("foo<<")
foo("_Var1Value","Q","W","E", _KeyWord1="_KeyWord1Value",_KeyWord2="_KeyWord2Value",_KeyWord3="_KeyWord3Value" )
##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")