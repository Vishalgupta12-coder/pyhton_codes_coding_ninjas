try:
  n1=4
  n2=2
  print(n1/0)
except ZeroDivisionError:
	print(unknowh_var)#error
finally:
	print("this is last")#this statement executes everytime



'''try:
  n1=4
  n2=2
  print(n2/n2)
  print("done")
except ZeroDivisionError:
	print("an error due to zero division")
print("finished")'''
	
	
	
try:
  n1=20
  print(n1/0)
  print(n1+"hello")
except ZeroDivisionError:
	print("number is divided by zero")
except (ValueError,TypeError):
	print("value error")


