
def printTable(start,end,step):
    for i in range(start,end+1,step):
        f=int((i-32)*(5/9))
        print(i,end="\t")
        print(f)

s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)


'''
6
1 2 3 4 5 6 
13 14 15 16 17 18 
25 26 27 28 29 30 
31 32 33 34 35 36 
19 20 21 22 23 24 
7 8 9 10 11 12

n = int(input())
for i in range((n+1)//2):
       for j in range(1,n+1):
             print(n*2*i + j ,end = " ");
       print()
for i in range(n//2,0,-1):  
        for j in range (1,n+1):
             print(n*(2*i-1) +j, end = " ")
        print()'''

'''5
12345
 2345
  345
   45
    5
   45
  345
 2345
12345

num=int(input())
i=0
while num>i:
    spaces=1
    while spaces<=i:
        print(" ",end="")
        spaces=spaces+1
    j=1
    while num-i >=j:
        print(j+i,end="")
        j=j+1
    i=i+1
    print()
while i>1:
    spaces=1
    while spaces<=i-2:
        print(" ",end="")
        spaces=spaces+1
    j=num
    k=1
    while j>=i-1:
        print(i+k-2,end="")
        j=j-1
        k=k+1

    i=i-1
    print()'''




'''n=int(input())
n1=(n+1)/2
n2=n/2
i=1
while i<=n1:
	space=1
	while space<=i-1:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=i:
	      print('*',end="")	
	      j=j+1
	print()
	i=i+1
i=1		     
while i<=n1:
	space=1
	while space<=n1-i-1:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=n1-i:
	      print('*',end="")	
	      j=j+1		     
	print()
	i=i+1'''


'''
n=9
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *


n=int(input())
n1=n/2
n2=(n+1)/2
i=1
while i<=n2:
	space=1
	while space<=n2-i:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=i:
	      print('*',end="")	
	      j=j+1
	p=i-1
	while p>=1:
		print('*',end="")
		p=p-1		     
	print()
	i=i+1
i=1
while i<=n1:
	space=n1
	while space>=n1-i+1:
	      print(' ',end="")	
	      space=space-1
	j=n-2
	while j>=2*i-1:
	      print('*',end="")	
	      j=j-1
			     
	print()
	i=i+1'''

	
	

	
	
	








		
			     
               