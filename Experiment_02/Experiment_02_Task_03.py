# Student Name : Aman Sagar
# Roll_Number : 2024ug3015
# Course : CD-2101-Python Programming Lab
# Experiment-2-Task_03 : Making Valid Password

temp=True #to run loop until valid password is entered
while temp:
    user_password = input("Enter a password: ") #taking input password
    if len(user_password) < 8:#checking length of password
        print("Password is too short. It must be at least 8 characters long.")
        continue #restart loop if length is less than 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "@#$%^&*!"
    for char in user_password:
        if char.isupper():#checking for uppercase letter
            has_upper = True
        elif char.islower():#checking for lowercase letter
            has_lower = True
        elif char.isdigit():#checking for digit
            has_digit = True
        elif char in special_chars:#checking for special character
            has_special = True
    if has_upper and has_lower and has_digit and has_special:#checking all conditions
        print("Password is valid.") 
        temp=False #to exit loop
        
    else:
        print("Password is invalid. It must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (@, #, $, %, ^, &, *, !).")