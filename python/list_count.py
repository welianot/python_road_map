fruits=[]
count=0
for i in range (5):
    f=input(f"enter the  names of fruits of {i}th item")
    fruits.append(f)
search_fruit=input (f"Enter the fruits to be searched")
for fruit in fruits:
    if fruit==search_fruit:
      count+=1
if (count>0):      
 print(f"The fruit you searched {search_fruit} is occuring \n {count} times \n in the list {fruits}\n at index {fruits.index(search_fruit)}")      