students = {}

while True:
    print("\n1. Add a Student")
    print("2. Assign Grades")
    print("3. View Grades")
    print("4. Delete a Student")
    print("5. Display All Students")
    print("6. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        student_id = int(input("Enter student ID: "))
        if student_id in students:
            print("Student already exists!")
        else:
            name = input("Enter student name: ")
            students[student_id] = {'name': name, 'grades': []}
            print("Student added successfully!")
    
    elif ch == 2:
        student_id = int(input("Enter student ID: "))
        if student_id in students:
            print(f"Assigning grades for {students[student_id]['name']}")
            grades = list(map(float, input("Enter grades separated by spaces: ").split()))
            students[student_id]['grades'].extend(grades)
            print("Grades added successfully!")
        else:
            print("Student not found!")
    
    elif ch == 3:
        student_id = int(input("Enter student ID: "))
        if student_id in students:
            print(f"Grades for {students[student_id]['name']}: {students[student_id]['grades']}")
        else:
            print("Student not found!")
    
    elif ch == 4:
        student_id = int(input("Enter student ID to delete: "))
        if student_id in students:
            del students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")
    
    elif ch == 5:
        if students:
            print("\nAll Students and Their Grades:")
            for student_id, info in students.items():
                print(f"ID: {student_id}, Name: {info['name']}, Grades: {info['grades']}")
        else:
            print("No students found!")
    
    elif ch == 6:
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")
