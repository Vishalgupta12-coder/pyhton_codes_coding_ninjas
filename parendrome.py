def checkPalindrome(num):
#Implement Your Code Here
    temp=num
    rev=0
    while num!=0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
        if temp==rev:
           return True	
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
