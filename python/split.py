nums=[]
odd=[]
even=[]
for i in range(10):
    n=int(input("Enter the numbers"))
    nums.append(n)
for num in nums :
    if num%2==0: 
        even.append(num)
    else:
        odd.append(num)
print(f"The odd numbers are {odd} with {odd.count} number\n even numbers are {even} with {even.count} number")               

