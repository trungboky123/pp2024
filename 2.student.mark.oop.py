class Person:
    def __init__(self, id, name, dob=None):
        self.id = id
        self.name = name
        self.dob = dob
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}" if self.dob else f"ID: {self.id}, Name: {self.name}"
class Student(Person):
    pass
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"
class MarkManager:
    def __init__(self):
        self.marks = {}

    def input_mark(self, students, course):
        print(f"Entering marks for course: {course.name}")
        for student in students:
            try:
                mark = float(input(f"Enter mark for {student.name} ({student.id}): "))
                if course.id not in self.marks:
                    self.marks[course.id] = {}
                self.marks[course.id][student.id] = mark
            except ValueError:
                print("Invalid input. Skipping this student.")
    def show_marks(self, students, course):
        print(f"Marks for course: {course.name}")
        if course.id in self.marks:
            for student in students:
                mark = self.marks[course.id].get(student.id, "Not entered")
                print(f"{student.name} ({student.id}): {mark}")
        else:
            print("No marks available for this course.")
class UniversityManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.mark_manager = MarkManager()
    def input_students(self):
        try:
            num = int(input("Enter the number of students: "))
            for _ in range(num):
                id = input("Enter student ID: ")
                name = input("Enter student name: ")
                dob = input("Enter student DoB: ")
                self.students.append(Student(id, name, dob))
        except ValueError:
            print("Invalid input")
    def input_courses(self):
        try:
            num = int(input("Enter the number of courses: "))
            for _ in range(num):
                id = input("Enter course ID: ")
                name = input("Enter course name: ")
                self.courses.append(Course(id, name))
        except ValueError:
            print("Invalid input")

    def list_students(self):
        print("--- List of Students ---")
        for student in self.students:
            print(student)
    def list_courses(self):
        print("--- List of Courses ---")
        for course in self.courses:
            print(course)
    def input_marks(self):
        self.list_courses()
        course_id = input("Enter the course ID to input marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if course:
            self.mark_manager.input_mark(self.students, course)
        else:
            print("Invalid course ID.")
    def show_marks(self):
        self.list_courses()
        course_id = input("Enter the course ID to show marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if course:
            self.mark_manager.show_marks(self.students, course)
        else:
            print("Invalid course ID.")
    def run(self):
        while True:
            print("--- University Management System ---")
            print("0. Exit")
            print("1. Input Students")
            print("2. Input Courses")
            print("3. List Students")
            print("4. List Courses")
            print("5. Input Marks")
            print("6. Show Marks")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    print("Exiting program.")
                    break
                elif choice == 1:
                    self.input_students()
                elif choice == 2:
                    self.input_courses()
                elif choice == 3:
                    self.list_students()
                elif choice == 4:
                    self.list_courses()
                elif choice == 5:
                    self.input_marks()
                elif choice == 6:
                    self.show_marks()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
if __name__ == "__main__":
    UMS = UniversityManagementSystem()
    UMS.run()