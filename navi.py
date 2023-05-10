'''lst =[2, 8, 9, 11, -55, -11, 22, 78, 67]

length = len (lst) 
element= int(input("Enter element to be searched for :"))
a=lst.index(element)
print(str(element)+" found at index "+str(a))

st = ['p', 'y', 't', 'h', 'o','n']
print("Given list is",st) 
print (type(st)) 
str1=''.join(st)
print("After converting list to the string=",str1)
print (type(str1))


class point3D(object):
      def __init__(self,x,y,z):
            self.x=x
            self.y=y 
            self.z=z
      def __repr__(self) :

            return "(%d, %d, %d)" % (self.x, self.y, self.z) 
my_point=point3D(1,2,3) 
print (my_point)

n=int(input("Please input numbers to find their maximum and press -1 to terminate calculation\n"))
maximum=n
def max(i, j):
	if j>i:
		return j
	else:
		return i
while n!=-1:
       n=int(input("Please input next number\n"))
       maximum=max(maximum, n)
print("maximum is:", maximum)'''

'''userinput=input("Please input your text to print it's reverse\n") 
def reverse(userinput): 

  str = "" 

  for i in userinput: 

    str = i + str

  return str
print ("Your inputted string is: ",userinput)

print ("The reverse of the inputted string is:",str)




s = input("Please input your text to print it's reverse ")

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
print ("Your inputted string is: ",s) 
print ("The reverse of the inputted string is:",end="") 
print (reverse(s))

userinput=input("Please input your text to print it's reverse\n") 
def reverse(userinput): 

  str = "" 

  for i in userinput: 

    str = i + str

  return str
print ("Your inputted string is: ",userinput)

print ("The reverse of the inputted string is: ",reverse(userinput))'''
'''


x=int(input("Please input the number to check for even or odd")) 

if(x%2==0):
      print("The given number is even")
else:
      print("The given number is odd")


'''

sum=0
print("The first n positive numbers having the total sum less than 100 are:") 
for i in range(1,100): 
       sum=sum+i
       if sum>100:
          break
       print(i,'',end='')
       
print("sum of the numbers = ",sum-i)
         
  
      


