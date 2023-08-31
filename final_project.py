# Final Project
# TODO 1
name = input("Enter Your Name :")
submission_data = input("Enter Your Submission Data :")
print("Name :", name)
print("Delivery :", submission_data)
print("Eng.Mohanad Alkruns")


import random
# TODO 2
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_mark = course_mark
# TODO 3
class Student:
    total_student = 0
# TODO 4
    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(10000, 99999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_student += 1
    # TODO 5
    def enroll_course(self,course_name,course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)
    # TODO 6
    def get_student_details(self):
        return {
            'Student_ID': self.student_id,
            'Name': self.student_name,
            'Age': self.student_age,
            'Number': self.student_number

        }
    # TODO 6
    def get_student_courses(self):
       for course in self.courses_list:
           print(f"Courses :{course.course_name} , Mark :{course.course_mark}")
    # TODO 7
    def get_student_average(self):
        if len(self.courses_list) == 0:
            return 0
        total_mark = sum(course.course_mark for course in self.courses_list)
        return total_mark/len(self.courses_list)
# TODO 8
student_list = []
# TODO 9
while True:
    try:
        selection = int(input("1- Add New Student \n"
                              "2- Delete Student\n"
                              "3- Display Student\n"
                              "4- Get Student Average\\n"
                              "5- Add Course To Student With Mark\n"
                              "6- Exit"))
        # TODO 10
        if selection == 1:
            student_number = input("Enter Student Number :")
            student_name = input("enter Student Name :")
            student_age = int(input("Enter Student Age :"))
            new_student = Student(student_name, student_age, student_number)
            student_list.append(new_student)
            print("Student Added Successfully")
        # TODO 11
        elif selection == 2:
            student_number = input("Enter Student Number :")
            for student in student_list:
                if student.student_number == student_number:
                    student_list.remove(student)
                    print("Student Deleted Successfully ")
                    break
            else:
                print("Student Not Exist")
        # TODO 12
        elif selection == 3 :
            student_number = input("Enter Student Number :")
            for student in student_list:
                if student.student_number == student_number:
                    print("Details Student :")
                    details = student.get_student_details()
                    for kye, value in details.items():
                        print(f"{kye} : {value}")
                    break
            else:
                print("Student Not Exist")
        # TODO 13
        elif selection == 4:
            student_number = input("Enter Student Number :")
            for student in student_list:
                if student.student_number == student_number:
                    average = student.get_student_average()
                    print(f"Average :{average}")
                    break
            else:
                print("Student Not Exist")
        # TODO 14
        elif selection == 5:
            student_number = input("Enter Student Number : ")
            for student in student_list:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name : ")
                    course_mark = float(input("Enter Course Mark : "))
                    student.enroll_course(course_name, course_mark)
                    print("Added Course Successfully")
                    break
            else:
                print("Student Not Exist")
        # TODO 15
        elif selection == 6:
            print("Exit")
        else:
            print("Selection Not True ")
    except ValueError:
        print("Please Enter True Value")









