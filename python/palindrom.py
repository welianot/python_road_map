text=input("Enter the string")
rev_text=text[::-1]
if text==rev_text:
    print(f"{text} is a palindrome")
else:
    print(f"not a palindrome")    