import os
if os.path.abspath(os.curdir) == os.path.dirname(os.path.realpath(__file__)) :
	os.system("start notepad++ "+__file__)
	exit()
##########################################################
arr = [1, 4, 9, 16, 25]
print(arr)
print(arr[0],arr[1],arr[2],arr[3],arr[4])
print(arr[-5],arr[-4],arr[-3],arr[-2],arr[-1])
print(arr[0:2],arr[2:5]) #а сдесь конец интервала входит
print(arr[:2],arr[2:4],arr[4:])
print(arr[:2]+arr[2:4]+arr[4:])
print('len(arr)=',len(arr))
#Массивы являются изменяемыми
arr.append(6)
print(arr)
print('len(arr)=',len(arr))

##########################################################
test_text = input(" Для завершения программы нажмите Enter: ")
