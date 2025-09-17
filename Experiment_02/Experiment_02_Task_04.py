# Student Name : Aman Sagar
# Roll_Number : 2024ug3015
# Course : CD-2101-Python Programming Lab
# Experiment-2-Task_04 : Finding the department of an Assistant Professor in IIIT Ranchi 


iiit_ranchi = { # Dictionary representing IIIT Ranchi's structure
    "Departments": { # Nested dictionary for departments
        "Computer Science & Engineering": {
            "Assistant Professors": [
            "Dr. Santosh Kumar Mahto",
            "Dr. Dhananjoy Bhakta",
            "Dr. Jayadeep Pati",
            "Dr. Shashi Kant Sharma",
            "Dr. Jitendra Kumar Mishra",
            "Dr. Roshan Singh",
            "Dr. Rajiv Kumar",
            "Dr. Rashmi Panda",
            "Dr. Bharat Singh",
            "Dr. Puja Ghosh",
            "Dr. Priyank Khare",
            "Dr. Kirti Kumari",  
            "Dr. Tarun Biswas",
            "Dr. Sandhir Kumar Singh",
            "Dr. Rohit Kandulna",
            "Dr. Rishikesh Dutta Tiwary",
            "Dr. Priyabrat Garanayak",
            "Dr. Nishit Malviya",
            "Dr. Ravi Shanker",
            "Dr. Abhinav Kumar",
            "Dr. Anuj Singh",
            "Dr. Chandra Prakash Singh"

            ]
        },
        "Electronics & Communication Engineering": {
            "Assistant Professors": [
            "Dr. Santosh Kumar Mahto",
            "Dr. Shashi Kant Sharma",
            "Dr. Jitendra Kumar Mishra",
            "Dr. Roshan Singh",
            "Dr. Rajiv Kumar",
            "Dr. Rashmi Panda",
            "Dr. Puja Ghosh",
            "Dr. Priyank Khare",

            ]
        },
        "Sciences": {
            "Head": "Dr. Sandhir Kumar Singh",
            "Assistant Professors": [
                "Dr. Sandhir Kumar Singh",
                "Dr. Noopur",
            ]
        },
        "Humanities & Management": {
            "Head": "Dr. (Name of HoD HM)",
            "Assistant Professors": [
                "Dr. Noopur",
            ]
        }
    }
}
prof_name = input("Enter the name of an Assistant Professor: ").strip() # Taking input and stripping extra spaces

found = False
departments = iiit_ranchi["Departments"] # Accessing the departments dictionary

# Iterate through all departments
for dept_name, dept_info in departments.items():
    if prof_name in dept_info["Assistant Professors"]: # Check if the professor is in the list
        print(f"{prof_name} belongs to the {dept_name} department.")
        found = True
        break

if not found:
    print(f"Assistant Professor named {prof_name} was not found in IIIT Ranchi’s structure.")
