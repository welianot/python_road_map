a=[]
b=[]
c=[]
for i in range (5):
    a1=int(input(f"Enter the numbers for a {i} th index "))
    a.append(a1)
for i in range (5):
    b1=int(input(f"Enter the numbers for b {i} th index "))
    b.append(b1)    
for a2 in a:
    for b2 in b:
        if a2==b2:
            c.append(a2)
print(f"The common are {c}")
