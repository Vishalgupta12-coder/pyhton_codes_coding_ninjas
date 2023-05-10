n=int(input())
t=n
s1=0
s2=0
while n!=0:
	d=n%10
	if d%2==0:
		s1=s1+d
	else:
		s2=s2+d
			
	n=n//10
print(s1,"",s2)

