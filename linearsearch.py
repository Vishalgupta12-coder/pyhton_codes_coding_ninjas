def lin_search(li,ele):
	for i in range(len(li)):
	    if li[i]==ele:
		    return ('element is present at loc ',i+1)
	return (ele,' not present in list')
		
n=int(input("enter no of elements : "))
li=[int(x) for x in input("enter elements : \n").split()]
ele=int(input("enter elements you want to search : "))
index=lin_search(li,ele)
print(index)


#without functions

'''n=int(input("enter no of elements : "))
li=[int(x) for x in input("enter elements : \n").split()]
ele=int(input("enter elements you want to search : "))
isFound=False
for i in range(len(li)):
	if li[i]==ele:
		print("element is present at loc ",i+1)
		isFound=True
		break 
if isFound is False:
	print(ele,' not present in list')'''