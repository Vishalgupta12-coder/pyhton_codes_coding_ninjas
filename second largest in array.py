'''def secondLargest(n, arr):
    x = arr[0]  
    if arr.count(x) == n or n<1:
        print(-2147483648)   
    else:
       arr.sort()
       m = max(arr)
       c = arr.count(m)        
       print(arr[n-1-c])
# Main
p=int(input())
while p>0:
 n=int(input())
 arr=[]
 if n>0:
  arr=[int(i) for i in input().split()[:n]]
  secondLargest(n, arr)
 p-=1'''





# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin
def secondLargestElement(arr, n):
    #Your code goes here

   # x = arr[0] 
 for i in arr: 
    if arr[0] == arr[i+1] or n<1:
        print(-2147483648)   
    else:
       arr.sort()
       m = max(arr)
       c = arr.count(m)        
       print(arr[n-1-c])


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1