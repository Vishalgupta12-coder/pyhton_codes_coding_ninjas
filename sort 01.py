def sort(ar):
    a = 0
    b = 0
    for i in ar:
        if i == 0:
            a+=1
        else:
            b+=1
    res = []
    for i in range(0, a):
        res.append(0)
    for i in range(0, b):
        res.append(1)
        
    for i in res:
        print(i, end = ' ')
k=1
p=int(input())
while k<=p:
 n = int(input())
 ar = [int(x) for x in input().split()[:n]]
 sort(ar)
 print()
 k=k+1