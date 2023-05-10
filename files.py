#file=open("abc.txt","r")
#print(file.readlines()) #to read lines

file=open("newfile.py","a")
file.write("\n some new content is added into the file ")
file.close()

#another way to read a file
with open("pattern1.py","r")as re:
 print(re.read())
re.close()


"""
msg="hello this is vishal"
file=open("newfile1.txt","w")
written=file.write(msg)
if (written==len(msg)):
	print("file created sucessfully")
else:
	print("file not created")
print(written)
file.close()


file=open("newfile.txt","w")
file.close()
#read all data 

#delete previous data from the file
file=open("newfile.txt","w")
file.write("\n some new content")
file.close()
#add data into previous data
file=open("newfile.py","a")
file.write("\n some new content is added into the file ")
file.close()







file=open("abc.txt","r")
print(file.readlines()) #to read lines
for line in file: # to print all lines
	print(line)
#c=file.read() to read full file
#print(c)
print(file.read(6))#to read some part of file
print(file.read(10))
print(file.read(4))
print(file.read())#remaining part
file.close()"""
