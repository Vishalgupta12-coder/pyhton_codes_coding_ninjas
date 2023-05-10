'''
n=6
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

'''n=5
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5 

N = int(input())

for i in range(1, N + 1):
	for j in range(1, N + 1):
		min = i if i < j else j
		print(N - min + 1, end = " ")

	for j in range(N - 1, 0, -1):
		min = i if i < j else j
		print(N - min + 1, end = " ")

	print()
	
for i in range(N - 1, 0, -1):
	for j in range(1, N + 1):
		min = i if i < j else j
		print(N - min + 1, end = " ")

	for j in range(N - 1, 0, -1):
		min = i if i < j else j
		print(N - min + 1, end = " ")

	print()'''


'''
n=5
  *
 ***
*****
 ***
  *

n=int(input())
k=(n+1)//2
l=n//2
i=1
for i in range(1,k+1,1):

	for s in range(k-i):
	        print(' ',end='')
	for j in range(i,2*i,1):
	        print('*',end='')
	for j in range(2*i-2,i-1,-1):
	        print('*',end='')
	print()
i=1
for i in range(1,l+1,1):

	for s in range(i,0,-1):
	        print(' ',end='')
	for j in range(2*l-i,i-1,-1):
		print('*',end='')
	
	print()'''

'''n=5
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


'''
111111
00000
1111
000
11
0

n=int(input())
i=1
for i in range(1,n+1,1):

	for s in range(n-i+1):
	     if(i%2==0):
	        print(0,end='')
	     else:
	        print(1,end='')
	print()'''

'''
#using for loop
n=5
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
i=1
for i in range(1,n1+1,1):

	for s in range(n-i):
	        print(' ',end='')
	for j in range(i,2*i,1):
	        print('*',end='')
	for j in range(2*i-2,i-1,-1):
	        print('*',end='')
	print()
i=1
for i in range(1,n+1,1):

	for s in range(i,0,-1):
	        print(' ',end='')
	for j in range(2*n-i-1,i,-1):
		print('*',end='')
	
	print()'''



'''n=9
*
 **
  ***
   ****
    *****
   ****
  ***
 **
*

n=int(input())
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
	      print('* ',end="")	
	      j=j+1
	print()
	i=i+1
i=1		     
while i<=n2:
	space=1
	while space<=n1-i-1:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=n1-i:
	      print('* ',end="")	
	      j=j+1		     
	print()
	i=i+1'''

'''n=5
 *
  **
   ***
    ****
     *****
    ****
   ***
  **
 *

n=int(input())
i=1
while i<=n:
	space=1
	while space<=i:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=i:
	      print('*',end="")	
	      j=j+1
	print()
	i=i+1
i=1		     
while i<=n:
	space=1
	while space<=n-i:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=n-i:
	      print('*',end="")	
	      j=j+1		     
	print()
	i=i+1'''
'''n=5
    1
   212
  32123
 4321234
543212345

n=int(input())
i=1
while i<=n:
	space=1
	while space<=n-i:
	      print(' ',end="")	
	      space=space+1
	p=i
	while p>=1:
		print(p,end="")
		p=p-1
	j=1
	while j<=i-1:
		print(j+1,end='')
		j=j+1		     
	print()
	i=i+1'''


'''
n=4
*000*000*
0*00*00*0
00*0*0*00
000***000

n=int(input())
i=1
j=1
while i<=n:
	j=1
	while j<=n:
	      if(i==j):
	
	           print('*',end="")
	      else:
	           print(0,end='')	
	      j=j+1
	j=j-1
	print('*',end="")
	while j>=1:
		if(i==j):
			print("*",end='')
		else:
			print(0,end='')
		j=j-1
				      
	print()
	i=i+1'''


'''n=5
1        1
12      21
123    321
1234  4321
1234554321


n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
	      print(j,end="")	
	      j=j+1
		      
	space=1
	while space<=n-i:
	      print(' ',end="")	
	      space=space+1
	space=1
	while space<=n-i:
	      print(' ',end="")	
	      space=space+1
	p=i
	while p>=1:
		print(p,end="")
		p=p-1	      
	print()
	i=i+1'''


'''n=9
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

'''
n=5
    1
   232
  34543
 4567654
567898765


n=int(input())
i=1
while i<=n:
	space=1
	while space<=n-i:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=i:
	      print(i+j-1,end="")	
	      j=j+1
	p=i-1
	while p>=1:
		print(j+p-2,end="")
		p=p-1		     
	print()
	i=i+1'''





'''
n=6
     *
    ***
   *****
  *******
 *********
***********



n=int(input())
i=1
while i<=n:
	space=1
	while space<=n-i:
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
	i=i+1'''

''' 1
   121
  12321
 1234321
123454321

n=int(input())
i=1
while i<=n:
	space=1
	while space<=n-i:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=i:
	      print(j,end="")	
	      j=j+1
	p=i-1
	while p>=1:
		print(p,end="")
		p=p-1		     
	print()
	i=i+1'''
#mirror	
'''
    1
   12
  123
 1234
12345

n=int(input())
i=1
while i<=n:
	space=1
	while space<=n-i:
	      print(' ',end="")	
	      space=space+1
	j=1
	while j<=i:
	      print(j,end="")	
	      j=j+1	      
	print()
	i=i+1'''


'''
4
43
432
4321

n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
	      print(n-j+1,end="")	
	      j=j+1	      
	print()
	i=i+1
'''




'''
4321
321
21
1

n=int(input())
i=1
while i<=n:
	j=n
	while j>=i:
	      print(j-i+1,end="")	
	      j=j-1	      
	print()
	i=i+1
'''	
'''
1
21
321
4321

n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
	      print(i-j+1,end="")	
	      j=j+1	      
	print()
	i=i+1
'''	
	
'''	
*
**
***
****

n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
	      print("*",end="")	
	      j=j+1	      
	print()
	i=i+1
	
'''
'''

1
23
345
4567

n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
	      print(i+j-1,end="")	
	      j=j+1	      
	print()
	i=i+1
	


'''
'''
1
21
321
4321
54321
	
N=int(input())
s=''
i=1
while i <= N:
    s = str(i)+s
    print(s) 
    i=i+1    '''
'''
55555
4444
333
22
1

n=int(input())
i=1
while i<=n:
	j=1
	while j<=n-i+1:
	      print(n-i+1,end="")	
	      j=j+1	      
	print()
	i=i+1
#or

n=int(input())
i=1
while i<=n:
	j=n
	while j>=i:
	      print(n-i+1,end="")	
	      j=j-1	      
	print()
	i=i+1'''


#4th
"""A
BB
CCC
DDDD
EEEEE


n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
	      print(chr(ord('A')+i-1),end="")	
	      j=j+1	      
	print()
	i=i+1"""


"""#3rd
12345
1234
123
12
1


n=int(input())
i=1
while i<=n:
	j=n
	while j>=i:
	      print(n-j+1,end="")	
	      j=j-1	      
	print()
	i=i+1"""


'''#ist
1
11
202
3003
40004

n = int(input())
i=1
while i<=n:
    j=0
    while j<i:
        if i==1:
            print(1, end="")
        elif j and j<i-1:
            print(0, end="")
        else:
            print(i-1, end='')
        j=j+1
    print()
    i=i+1'''

#2nd
'''
1
11
121
1221
12221


n = int(input())
i=1
while i<=n:
    j=0
    while j<i:
        if i==1:
            print(1, end="")
        elif j and j<i-1:
            print(2, end="")
        else:
            print(1, end='')
        j=j+1
    print()
    i=i+1'''