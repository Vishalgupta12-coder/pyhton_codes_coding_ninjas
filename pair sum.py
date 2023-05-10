def pairSum(ar, n, x):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if ar[i]+ar[j] == x:  
                count=count+1
    print(count)  
k=1
p=int(input())
while k<=p:       
 n = int(input())
 ar=[]
 if n>0:
  ar = [int(x) for x in input().split()[:n]]
 x = int(input())
 pairSum(ar, n, x)
 k=k+1



'''
1
6
0 4 1 2 5 4 
5

def pairSum(ar, n, x):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if ar[i]+ar[j] == x:
                if ar[i] < ar[j]:
                    print(ar[i],ar[j])    
                else:
                    print(ar[j],ar[i])  
                count=count+1
    print(count)         
n = int(input())
ar = [int(x) for x in input().split()[:n]]
x = int(input())
pairSum(ar, n, x)'''