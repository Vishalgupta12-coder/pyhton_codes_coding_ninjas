'''
def pushToEnd(ar):
    res = []
    for i in range(len(ar)):
        if ar[i] != 0:
            res.append(ar[i])
            
    val = len(ar) - len(res)
    for i in range(val):
        res.append(0)
        
    for ele in res:
        return ele
p=int(input())
while p>0:   
 n = int(input())
 ar = [int(x) for x in input().split()[:n]]
 pushToEnd(ar)
 print()
 p-=1
'''





from sys import stdin

def pushZerosAtEnd(arr) :
    #Your code goes here
    res = []
    for i in range(len(arr)):
        if arr[i] != 0:
            res.append(arr[i])
            
    val = len(arr) - len(res)
    for i in range(val):
        res.append(0)
    return res
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()
    
    ans=pushZerosAtEnd(arr)
    for ele in ans:
       print(ele,end=' ')
   # printList(arr,n)

    t -= 1