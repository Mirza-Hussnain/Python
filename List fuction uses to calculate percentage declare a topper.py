def calculate_percentage(marks):
    total_marks = sum(marks)
    return (total_marks / len(marks))

students = []

names = ["Ali", "Asad", "Afgham", "Talha", "Sajid", "Imran", "Adeel", "Salman", "Mehwish", "Fatima"]
marks_list = [65, 77, 76, 56, 89, 87, 76, 89, 91, 87]

for i in range(len(names)):
    name = names[i]
    marks = [marks_list[i]]
    percentage = calculate_percentage(marks)
    students.append({"name": name, "marks": marks, "percentage": percentage})

print("\nStudent Details:")
topper = students[0]  # Assume the first student is the topper initially

for student in students:
    print(f"Name: {student['name']}")
    print(f"Marks: {student['marks'][0]}")
    print(f"Percentage: {student['percentage']:.2f}%")
    print()

    if student['percentage'] > topper['percentage']:
        topper = student

print(f"The topper is: {topper['name']} with a percentage of {topper['percentage']:.2f}%")
