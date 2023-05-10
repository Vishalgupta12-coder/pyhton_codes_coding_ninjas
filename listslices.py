
list=[]
n=int(input("enter no of elements "))
for i in range(0,n):
	l=input("Enter element : ")
	list.append(l)
print("Element are ",list)


squares=[0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[0:1])
print(squares[3:8])
print(squares[:8])
print(squares[5:])
print(squares[3:8:2])
print(squares[::3])
print(squares[::-1])#reverse a list=