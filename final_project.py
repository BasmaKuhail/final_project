import uuid

"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Basma M. Kuhail
Delivery Date : 22. June. 2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)


class Course:
    # counter = 1

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.id = str(uuid.uuid4())
        # another way: create a counter and update it each time we create an object:

        # self.id = Course.counter
        # Course.counter += 1


class Student:
    # TODO 3 define static variable indicates total student count
    total_std_count = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number, courses_list):
        # update total_std_count
        Student.total_std_count += 1

        self.student_id = str(uuid.uuid4())
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for course in self.courses_list:
            print(f"course name: {course.name}, course mark: {course.mark}")

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        sum_marks = 0
        for course in self.courses_list:
            sum_marks += course.mark

        return sum_marks / len(self.courses_list)


# in Global Scope
# TODO 8 declare empty students list
# we will add objects of types Student in it
students = []


def search_student_number(std_number):
    std_number_exist = False
    # loop over students list to look for similar student number
    for std in students:
        if std.student_number == std_number:
            std_number_exist = True
    return std_number_exist


def get_student_form_number(std_number):
    for std in students:
        if std.student_number == std_number:
            return std
    return None


def input_student_number():
    # to make sure they enter a number
    while True:
        try:
            student_number = int(input("Enter Student Number "))
            break
        except:
            print("Enter a number")
    return student_number


while True:
    # TODO 9 handle Exception for selection input

    while True:
        try:
            selection = int(input("\n1.Add New Student\n"
                                  "2.Delete Student\n"
                                  "3.Display Student\n"
                                  "4.Get Student Average\n"
                                  "5.Add Course to student with mark.\n"
                                  "6.Exit\n"))
            if (selection > 0) and (selection < 7):
                break
            else:
                print(" >Please enter a number from 1 to 6")
        except:
            print(" >Please enter a number from 1 to 6")

    if selection == 1:

        # TODO 10 make sure that Student number is not exists before
        while True:
            student_number = input_student_number()

            if search_student_number(student_number):
                print(" >student number already exist, enter new number")
            else:
                break

        student_name = input("Enter Student Name ")
        while True:
            try:
                student_age = int(input("Enter Student Age "))
                break
            except:
                print(" >Invalid Value")

        # TODO 11 create student object and append it to students list
        std1 = Student(student_name, student_age, student_number, [])
        students.append(std1)
        print(" >Student Added Successfully")

    elif selection == 2:
        student_number = input_student_number()

        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
        if search_student_number(student_number):
            students.remove(get_student_form_number(student_number))
            print(" >Student Deleted")
        else:
            print(" >Student Not Exist")

    elif selection == 3:
        student_number = input_student_number()

        # TODO 13 find the target student using loops and print student details  if exist , if not print ("Student
        #  Not Exist")
        if search_student_number(student_number):
            print(get_student_form_number(student_number).get_student_details())
        else:
            print(" >No such student")

    elif selection == 4:
        student_number = input_student_number()
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not
        #  Exist")
        if search_student_number(student_number):
            print(get_student_form_number(student_number).get_student_average())
        else:
            print(" >No such student")

    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses

    else:
        # TODO 16 call a function to exit the program
        pass
