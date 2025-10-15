name=input("Enter the name your name");
maths=int(input ("Enter the grade for your maths_exam"));
science=int(input("Enter the grade for your scince_exam"));
english=int(input("Enter the grade for your english_exam"));
average=(maths+science+english)/3;
if (average >=90):
    grade="A"
elif (average>=75):
    grade="B"
elif (average>=50):
    grade="C"
else:
    grade="F"





print(f"The average of {name} is {average:.2f} & your grade is {grade}")


