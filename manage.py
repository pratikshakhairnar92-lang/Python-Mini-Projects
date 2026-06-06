students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")

        marks = float(input("Enter Marks Obtained (out of 500): "))

        percentage = (marks / 500) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        student = {
            "name": name,
            "roll": roll,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found!")
        else:
            print("\n===== STUDENT RECORDS =====")
            for student in students:
                print("--------------------------")
                print("Name       :", student["name"])
                print("Roll No    :", student["roll"])
                print("Marks      :", student["marks"])
                print("Percentage :", round(student["percentage"], 2), "%")
                print("Grade      :", student["grade"])

    elif choice == "3":
        search_name = input("Enter Student Name to Search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("\nStudent Found!")
                print("Name       :", student["name"])
                print("Roll No    :", student["roll"])
                print("Marks      :", student["marks"])
                print("Percentage :", round(student["percentage"], 2), "%")
                print("Grade      :", student["grade"])
                found = True

        if not found:
            print("Student Not Found!")

    elif choice == "4":
        delete_name = input("Enter Student Name to Delete: ")

        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You! Program Closed.")
        break

    else:
        print("Invalid Choice! Please Try Again.")