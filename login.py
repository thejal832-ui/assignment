# Student-Teacher Management System

teachers = {
    "teacher1": "1234"
}

students = {}


# ---------------- STUDENT REGISTRATION ----------------

def add_student():
    print("\n--- Add Student ---")

    username = input("Enter student username: ")

    if username in students:
        print("Student already exists!")
        return

    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")

    students[username] = {
        "name": name,
        "age": age,
        "course": course,
        "grades": {}
    }

    print("Student added successfully!")


# ---------------- ADD GRADES ----------------

def add_grades():
    print("\n--- Add Student Grades ---")

    username = input("Enter student username: ")

    if username not in students:
        print("Student not found!")
        return

    python = input("Enter Python grade: ")
    mathematics = input("Enter Mathematics grade: ")
    english = input("Enter English grade: ")

    students[username]["grades"] = {
        "Python": python,
        "Mathematics": mathematics,
        "English": english
    }

    print("Grades added successfully!")


# ---------------- VIEW STUDENTS ----------------

def view_students():
    print("\n--- Student List ---")

    if not students:
        print("No students available.")
        return

    for username, details in students.items():
        print("\nUsername:", username)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])
        print("Grades:", details["grades"])


# ---------------- STUDENT LOGIN ----------------

def student_login():
    print("\n--- Student Login ---")

    username = input("Enter username: ")

    if username not in students:
        print("Student not found!")
        return

    password = input("Enter password: ")

  
    if password != "1234":
        print("Wrong password!")
        return

    print("\nLogin successful!")
    print("Welcome", students[username]["name"])

    while True:

        print("\n--- Student Menu ---")
        print("1. View My Details")
        print("2. View My Grades")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- My Details ---")
            print("Name:", students[username]["name"])
            print("Age:", students[username]["age"])
            print("Course:", students[username]["course"])

        elif choice == "2":
            print("\n--- My Grades ---")

            grades = students[username]["grades"]

            if grades:
                for subject, grade in grades.items():
                    print(subject, ":", grade)
            else:
                print("Grades not added yet.")

        elif choice == "3":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")


# ---------------- TEACHER LOGIN ----------------

def teacher_login():

    print("\n--- Teacher Login ---")

    username = input("Enter teacher username: ")
    password = input("Enter teacher password: ")

    if username == "teacher1" and password == teachers["teacher1"]:

        print("\nTeacher login successful!")

        while True:

            print("\n--- Teacher Menu ---")
            print("1. Add Student")
            print("2. Add Student Grades")
            print("3. View Students")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_student()

            elif choice == "2":
                add_grades()

            elif choice == "3":
                view_students()

            elif choice == "4":
                print("Teacher logged out!")
                break

            else:
                print("Invalid choice!")

    else:
        print("Invalid teacher username or password!")


# ---------------- MAIN MENU ----------------

while True:

    print("\n==============================")
    print(" Student Management System")
    print("==============================")

    print("1. Teacher Login")
    print("2. Student Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        teacher_login()

    elif choice == "2":
        student_login()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")