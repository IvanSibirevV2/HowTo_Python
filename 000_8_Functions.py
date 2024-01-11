import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
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
test_text = input(" Для завершения программы нажмите Enter: ")
