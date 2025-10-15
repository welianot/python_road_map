text=input("Enter the text ")
count_v=0
count_c=0
for i in text:
    if i.isalpha():
     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        count_v+=1
     else :
        count_c+=1
print(f"The count of vowels is {count_v}\n consonants is {count_c}")