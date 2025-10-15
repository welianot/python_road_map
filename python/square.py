nums=[]
sq_nums=[]
n=int(input("enter the number of numbers to be entered "))
for i in range (n):
    ns=int(input(f"Enter the numbers please of {i} index "))
    nums.append(ns)
for j in nums:
    s=j*j
    sq_nums.append(s)
print(f"Your entered list is {nums} \n  squared list is {sq_nums}")
        

