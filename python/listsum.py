nums=[]
sum=0
for i in range (5):
    n=int(input(f"Enter the number please {i} th term"))
    nums.append(n)
for i in range(len(nums)):
    sum=sum +nums[i]
print(f"The sum is {sum}")    
print(f" Your inputs are {nums}")


    