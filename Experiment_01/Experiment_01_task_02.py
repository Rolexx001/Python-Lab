# Student Name : Aman Sagar
# Roll_Number : 2024ug3015
# Course : CD-2101-Python Programming Lab
# Experiment-1-Task2 : To make the Grade card on the basis of average of marks of three subject

Marks1=int(input("Marks of First Subject")) 
Marks2=int(input("Marks of Second Subject"))
Marks3=int(input("Marks of Third Subject"))
avg=(Marks1+nMarks2+Marks3)/3; #calculating average marks
if(avg>=90):
    print("A") # output A for above 90
elif(avg<90 and avg>=80):
    print("B") # output B for between 80 and 90
elif(avg<80 and avg>=70):
    print("C") # output C for between 70 and 80
elif(avg<70 and avg>=60):
    print("D") # output D for between 60 and 70
else:
    print("F") # output F for below 60
