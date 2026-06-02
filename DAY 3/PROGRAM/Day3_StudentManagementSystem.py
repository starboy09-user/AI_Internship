students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")

        students[roll_no] = {
            "Name": name,
            "Course": course
        }

        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for roll_no, details in students.items():
                print("\n----------------")
                print("Roll No :", roll_no)
                print("Name    :", details["Name"])
                print("Course  :", details["Course"])
        else:
            print("No Student Records Found!")

    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")

        if roll_no in students:
            print("\nStudent Found")
            print("Name   :", students[roll_no]["Name"])
            print("Course :", students[roll_no]["Course"])
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll_no = input("Enter Roll Number to Delete: ")

        if roll_no in students:
            del students[roll_no]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice!")