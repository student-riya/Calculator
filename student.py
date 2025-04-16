students = {}

# Taking user input for 10 students
for i in range(5):
    print(f"Enter details for student {i + 1}:")
    full_name = input("Full Name: ").strip()
    age = int(input("Age: "))
    department = input("Department: ").strip()
    cgpa = float(input("CGPA (out of 5): "))
    
    students[full_name] = {"Age": age, "Department": department, "CGPA": cgpa}

# Function to format names as initials with surname
def format_name(full_name):
    parts = full_name.split()
    return f"{parts[0][0]}. {parts[-1]}" if len(parts) > 1 else full_name

# (a) Print all student names in initials format
print("\nFinal Year Students (Initials with Surname):")
for name in students.keys():
    print(format_name(name))

# (b) Find the student with the highest CGPA
highest_cgpa_student = max(students.items(), key=lambda x: x[1]["CGPA"])
print(f"\nStudent with Highest CGPA: {format_name(highest_cgpa_student[0])}, Details: {highest_cgpa_student[1]}")

# (c) Display students with CGPA below 3.0
low_cgpa_students = [format_name(name) for name, details in students.items() if details["CGPA"] < 3.0]
if low_cgpa_students:
    print("\nStudents with CGPA below 3.0:", ", ".join(low_cgpa_students))
else:
    print("\nNo students with CGPA below 3.0.")
