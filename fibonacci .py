n=int(input())
n_1=1
n_2=1 
count=0
while count < n:  
        print(n_1) 
        nth = n_1 + n_2  
       # At last, we will update values  
        n_1 = n_2  
        n_2 = nth  
        count += 1 
print(n_1) 