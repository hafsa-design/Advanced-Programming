# Student data
students = [
    {"name": "Smith", "number": 1001, "coursework": 41, "exam": 80, "overall": 75.63, "grade": "A"},
    {"name": "David", "number": 1002, "coursework": 32, "exam": 70, "overall": 63.75, "grade": "B"},
    {"name": "Aleena", "number": 1003, "coursework": 45, "exam": 90, "overall": 84.38, "grade": "A"}
]

# Display each student's details
for student in students:
    print(f"Student Name = {student['name']}")
    print(f"Student Number = {student['number']}")
    print(f"Total coursework mark = {student['coursework']}")
    print(f"Exam Mark = {student['exam']}")
    print(f"Overall Percentage = {student['overall']}%")
    print(f"Student Grade = {student['grade']}")
    print("-" * 40)

# Number of students
num_students = len(students)
print(f"Number of students: {num_students}")

# Average percentage
total_percentage = sum(student['overall'] for student in students)
average_percentage = total_percentage / num_students
print(f"Average Percentage: {average_percentage:.2f}%")

# Student data
students = [
    {"name": "Smith", "number": 1001, "coursework": 41, "exam": 80, "overall": 75.63, "grade": "A"},
    {"name": "David", "number": 1002, "coursework": 32, "exam": 70, "overall": 63.75, "grade": "B"},
    {"name": "Aleena", "number": 1003, "coursework": 45, "exam": 90, "overall": 84.38, "grade": "A"}
]

# Display menu
print("Select a student to view details:")
for i, student in enumerate(students, start=1):
    print(f"{i}. {student['name']}")

# User input
choice = int(input("Enter the number of the student: "))

# Display selected student's details
if 1 <= choice <= len(students):
    student = students[choice - 1]
    print(f"\nStudent Name = {student['name']}")
    print(f"Student Number = {student['number']}")
    print(f"Total coursework mark = {student['coursework']}")
    print(f"Exam Mark = {student['exam']}")
    print(f"Overall Percentage = {student['overall']}%")
    print(f"Student Grade = {student['grade']}")
    print("-" * 40)
else:
    print("Invalid selection!")

# Student data
students = [
    {"name": "Smith", "number": 1001, "coursework": 41, "exam": 80, "overall": 75.63, "grade": "A"},
    {"name": "David", "number": 1002, "coursework": 32, "exam": 70, "overall": 63.75, "grade": "B"},
    {"name": "Aleena", "number": 1003, "coursework": 45, "exam": 90, "overall": 84.38, "grade": "A"}
]

# Find student with highest overall percentage
top_student = max(students, key=lambda s: s['overall'])

# Display the top student's details
print("Student with the highest overall mark:")
print(f"Student Name = {top_student['name']}")
print(f"Student Number = {top_student['number']}")
print(f"Total coursework mark = {top_student['coursework']}")
print(f"Exam Mark = {top_student['exam']}")
print(f"Overall Percentage = {top_student['overall']}%")
print(f"Student Grade = {top_student['grade']}")
print("-" * 40)

# Student data
students = [
    {"name": "Smith", "number": 1001, "coursework": 41, "exam": 80, "overall": 75.63, "grade": "A"},
    {"name": "David", "number": 1002, "coursework": 32, "exam": 70, "overall": 63.75, "grade": "B"},
    {"name": "Aleena", "number": 1003, "coursework": 45, "exam": 90, "overall": 84.38, "grade": "A"}
]

# Find student with lowest overall percentage
lowest_student = min(students, key=lambda s: s['overall'])

# Display the lowest student's details
print("Student with the lowest overall mark:")
print(f"Student Name = {lowest_student['name']}")
print(f"Student Number = {lowest_student['number']}")
print(f"Total coursework mark = {lowest_student['coursework']}")
print(f"Exam Mark = {lowest_student['exam']}")
print(f"Overall Percentage = {lowest_student['overall']}%")
print(f"Student Grade = {lowest_student['grade']}")
print("-" * 40)

# Student data
students = [
    {"name": "Smith", "number": 1001, "coursework": 41, "exam": 80, "overall": 75.63, "grade": "A"},
    {"name": "David", "number": 1002, "coursework": 32, "exam": 70, "overall": 63.75, "grade": "B"},
    {"name": "Aleena", "number": 1003, "coursework": 45, "exam": 90, "overall": 84.38, "grade": "A"}
]

# Sort students by overall percentage (descending)
sorted_students = sorted(students, key=lambda s: s['overall'], reverse=True)

# Display sorted student records
print("Sorted Student Records:")
for student in sorted_students:
    print(f"Student Name = {student['name']}")
    print(f"Student Number = {student['number']}")
    print(f"Total coursework mark = {student['coursework']}")
    print(f"Exam Mark = {student['exam']}")
    print(f"Overall Percentage = {student['overall']}%")
    print(f"Student Grade = {student['grade']}")
    print("-" * 40)

# Number of students
num_students = len(students)
print(f"Number of students: {num_students}")

# Average percentage
average_percentage = sum(s['overall'] for s in students) / num_students
print(f"Average Percentage: {average_percentage:.2f}%")

# New student details
student_code = 1004
student_name = "John"
coursework1 = 14
coursework2 = 15
coursework3 = 16
exam_mark = 85

# Calculate total coursework mark
total_coursework = coursework1 + coursework2 + coursework3

# Calculate overall percentage
# Assuming coursework is out of 60 (3 x 20) and exam out of 100
# Weighting: Coursework 40%, Exam 60% (as an example)
coursework_percentage = (total_coursework / 60) * 40
exam_percentage = (exam_mark / 100) * 60
overall_percentage = coursework_percentage + exam_percentage

# Determine grade
if overall_percentage >= 70:
    grade = "A"
elif overall_percentage >= 60:
    grade = "B"
elif overall_percentage >= 50:
    grade = "C"
elif overall_percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Display student's results
print(f"Student Name = {student_name}")
print(f"Student Number = {student_code}")
print(f"Total coursework mark = {total_coursework}")
print(f"Exam Mark = {exam_mark}")
print(f"Overall Percentage = {overall_percentage:.2f}%")
print(f"Student Grade = {grade}")
print("-" * 40)

# Current student data
students = [
    {"name": "Smith", "number": 1001, "coursework": 41, "exam": 80, "overall": 75.63, "grade": "A"},
    {"name": "David", "number": 1002, "coursework": 32, "exam": 70, "overall": 63.75, "grade": "B"},
    {"name": "Aleena", "number": 1003, "coursework": 45, "exam": 90, "overall": 84.38, "grade": "A"}
]

# Delete student by name
student_to_delete = "David"
students = [s for s in students if s['name'] != student_to_delete]

# Display updated student records
print("Updated Student Records:")
for student in students:
    print(f"Student Name = {student['name']}")
    print(f"Student Number = {student['number']}")
    print(f"Total coursework mark = {student['coursework']}")
    print(f"Exam Mark = {student['exam']}")
    print(f"Overall Percentage = {student['overall']}%")
    print(f"Student Grade = {student['grade']}")
    print("-" * 40)

# Updated number of students
num_students = len(students)
print(f"Number of students: {num_students}")

# Updated average percentage
average_percentage = sum(s['overall'] for s in students) / num_students
print(f"Average Percentage: {average_percentage:.2f}%")

# Current student data
students = [
    {"name": "Smith", "number": 1001, "coursework1": 12, "coursework2": 14, "coursework3": 15, "exam": 80},
    {"name": "David", "number": 1002, "coursework1": 10, "coursework2": 12, "coursework3": 10, "exam": 70},
    {"name": "Aleena", "number": 1003, "coursework1": 15, "coursework2": 15, "coursework3": 15, "exam": 90}
]

# Function to update student
def update_student(student_number):
    # Find the student
    student = next((s for s in students if s['number'] == student_number), None)
    if not student:
        print("Student not found!")
        return
    
    print("Enter new data (leave blank to keep current value):")
    code = input(f"Code ({student['number']}): ")
    name = input(f"Name ({student['name']}): ")
    cw1 = input(f"Coursework 1 ({student['coursework1']}): ")
    cw2 = input(f"Coursework 2 ({student['coursework2']}): ")
    cw3 = input(f"Coursework 3 ({student['coursework3']}): ")
    exam = input(f"Exam ({student['exam']}): ")
    
    # Update values if provided
    if code: student['number'] = int(code)
    if name: student['name'] = name
    if cw1: student['coursework1'] = int(cw1)
    if cw2: student['coursework2'] = int(cw2)
    if cw3: student['coursework3'] = int(cw3)
    if exam: student['exam'] = int(exam)
    
    print("Student updated successfully.")

# Example usage
update_student(1001)

# Display updated student
student = next(s for s in students if s['number'] == 1001)
print("\nUpdated Student Record:")
print(f"Student Name = {student['name']}")
print(f"Student Number = {student['number']}")
print(f"Coursework 1 = {student['coursework1']}")
print(f"Coursework 2 = {student['coursework2']}")
print(f"Coursework 3 = {student['coursework3']}")
print(f"Exam = {student['exam']}")
print("-" * 40)
