# Student Management System

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    student = {
        "Roll": roll,
        "Name": name,
        "Marks": marks 
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 40)
    for student in students:
        print(f"Roll No : {student['Roll']}")
        print(f"Name    : {student['Name']}")
        print(f"Marks   : {student['Marks']}")
        print("-" * 40)

def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found")
            print(f"Roll No : {student['Roll']}")
            print(f"Name    : {student['Name']}")
            print(f"Marks   : {student['Marks']}")
            return

    print("Student not found.")

def update_student():
    roll = input("Enter Roll Number to update: ")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Marks"] = float(input("Enter New Marks: "))
            print("Student record updated successfully!")
            return

    print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student record deleted successfully!")
            return

    print("Student not found.")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")