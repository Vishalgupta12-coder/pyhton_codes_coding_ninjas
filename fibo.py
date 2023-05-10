def checkMember(n):
#Implement Your Code Here
    a=0
    b=1
    if(n==0 or n==1):
          return True
    else:
        for i in range(0,n+1,1):
            c=a+b
            if(c == n):
              return True
            a = b;
            b = c;
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")