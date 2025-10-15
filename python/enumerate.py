names=[]
n=int(input("Enter the number of names to be entered"))
for i in range (n):
    ns=input("Enter the names")
    names.append(ns)
for i,name in enumerate(names):
    print(f"The name {name} is at index {i}")
