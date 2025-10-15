nums=[1, 2, 3, 4, 5, 6, 7, 8]
n=[]
sq=[]
for num in nums:
    if num%2==0:
        n.append(num)
for num in n:
    sq.append(num**2)
print(sq)            



