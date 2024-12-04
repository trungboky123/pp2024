def studentInfo():
    id = input("Enter student's ID:")
    name = input("Enter student's name:")
    dob = input("Enter student's date of birth: ")
    return {"id" : id, "name" : name, "dob" : dob}
def courseInfo():
    id = input("Course's ID is: ")
    name = input("Course's name is: ")
    return {"id" : id, "name" : name}
def numofStudents():
    num = int(input("Enter the number of students in a class:"))
    student = []
    for i in range(num):
        temp = studentInfo()
        student.append(temp)
    return student
def numofCourses():
    num = int(input("Enter the number of courses:"))
    course = []
    for i in range(num):
        temp = courseInfo()
        course.append(temp)
    return course
def listCourses(courses):
    print("\n---List of courses---")
    for course in courses:
        print("ID: {}, name: {}" .format(course['id'], course['name']))
def listStudents(students):
    print("\n---List of students---")
    for student in students:
        print("ID: {}, name: {}, dob: {}" .format(student['id'], student['name'], student['dob']))
def inputMarks(students, courses, marks):
    listCourses(courses)
    print("Enter the course id: ")
    course = input()
    if course not in marks:
        marks[course] = {}
    listStudents(students)
    print("Enter the student id to input mark: ")
    student = input()
    marks[course][student] = float(input("Enter mark: "))
    return marks
def showMarks(students, marks):
    course = input("What course do you want to see ?: ")
    
    if course not in marks or marks[course] == {}:
        print("This code haven't entered the mark")
    else:
        for student in students:
            if (student["id"] in marks[course]):
                print("Student id: {}, Mark: {}".format(student["id"], marks[course][student["id"]]))
            else:
                print("Student id: {}, Mark: Not entered".format(student["id"]))
marks = {}
while (True):
    print("---ENTER YOUR CHOICE---")
    print("--0. EXIT THE PROGRAM--")
    print("--1. INPUT STUDENTS----")
    print("--2. INPUT COURSES-----")
    print("--3. LIST COURSES------")
    print("--4. LIST STUDENTS-----")
    print("--5. INPUT MARK--------")
    print("--6. SHOW MARK---------\n")

    choice = int(input())
    if (choice == 0):
        break
    elif (choice == 1):
        students = numofStudents()
    elif (choice == 2):
        courses = numofCourses()
    elif (choice == 3):
        listCourses(courses)
    elif (choice == 4):
        listStudents(students)
    elif (choice == 5):
        marks = inputMarks(students,courses, marks)
    elif (choice == 6):
        showMarks(students, marks)
    else:
        print("Invalid choice")