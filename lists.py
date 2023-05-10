
n=int(input())
sum=0
li=list(map(input().strip().split()))[:n]
for i in range(0,len(li)):
	sum=sum+int(li[i])
print(sum)



'''n = int(input("Enter number of elements : "))
# Below line read inputs from user using map() function
a = list(map(int,input("nEnter the numbers : ").strip().split()))[:n]
print("nList is - ", a)
'''




'''
n=int(input())
li=[]
sum=0
for i in range(0,n):
    li.insert(0,input().split())
for i in range(0,len(li)):
	sum=sum+int(li[i])
print(sum)
'''