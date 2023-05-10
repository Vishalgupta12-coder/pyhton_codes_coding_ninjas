n=int(input())
i=1
while i<=n:
	j=1
	start=chr(ord('A')+n)
	while j<=i:
	      k=ord(start)+j-i
	      print(chr(k-1),end="")	
	      j=j+1	      
	print()
	i=i+1