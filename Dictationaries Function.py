# Creating dictionaries for students
student1 = {
    "name": "Alice",
    "age": 18,
    "grade": "A",
    "city": "New York"
}

student2 = {
    "name": "Bob",
    "age": 17,
    "grade": "B",
    "city": "Los Angeles"
}

# ... (similarly, define dictionaries for student3 to student10)

# Storing dictionaries in a list
students = [student1, student2]

# Displaying information for each student
for i, student in enumerate(students, start=1):
    print(f"Student {i}:")
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Grade:", student["grade"])
    print("City:", student["city"])
    print()
