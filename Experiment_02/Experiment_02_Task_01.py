# Student Name : Aman Sagar
# Roll_Number : 2024ug3015
# Course : CD-2101-Python Programming Lab
# Experiment-2-Task_01 : Grouping people based on age


age = int(input("Enter your age: "))#taking input age
        
if age < 0:
    print("Invalid age. Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior.")