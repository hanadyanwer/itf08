import random

class Course:
    def __init__(self, name, mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = name
        self.course_mark = mark

class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(10000, 99999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1
        pass

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    def get_student_details(self):
        return {
            'Student ID': self.student_id,
            'Name': self.student_name,
            'Age': self.student_age,
            'Number': self.student_number
        }

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")
            pass

    def get_student_average(self):
        if len(self.courses_list) == 0:
            return 0
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)

students_list = []

while True:
    try:
        selection = int(input("1. إضافة طالب جديد\n"
                              "2. حذف طالب\n"
                              "3. عرض بيانات طالب\n"
                              "4. الحصول على معدل طالب\n"
                              "5. إضافة مقرر للطالب مع العلامة\n"
                              "6. الخروج\n"))

        if selection == 1:
            student_number = input("أدخل رقم الطالب: ")
            student_name = input("أدخل اسم الطالب: ")
            student_age = int(input("أدخل عمر الطالب: "))
            new_student = Student(student_name, student_age, student_number)
            students_list.append(new_student)
            print("تمت إضافة الطالب بنجاح")

        elif selection == 2:
            student_number = input("أدخل رقم الطالب: ")
            for student in students_list:
                if student.student_number == student_number:
                    students_list.remove(student)
                    print("تم حذف الطالب بنجاح")
                    break
            else:
                print("الطالب غير موجود")

        elif selection == 3:
            student_number = input("أدخل رقم الطالب: ")
            for student in students_list:
                if student.student_number == student_number:
                    print("بيانات الطالب:")
                    details = student.get_student_details()
                    for key, value in details.items():
                        print(f"{key}: {value}")
                    break
            else:
                print("الطالب غير موجود")

        elif selection == 4:
            student_number = input("أدخل رقم الطالب: ")
            for student in students_list:
                if student.student_number == student_number:
                    average = student.get_student_average()
                    print(f"معدل الطالب: {average}")
                    break
            else:
                print("الطالب غير موجود")

        elif selection == 5:
            student_number = input("أدخل رقم الطالب: ")
            for student in students_list:
                if student.student_number == student_number:
                    course_name = input("أدخل اسم المقرر: ")
                    course_mark = float(input("أدخل العلامة: "))
                    student.enroll_course(course_name, course_mark)
                    print("تمت إضافة المقرر بنجاح")
                    break
        elif selection == 6:
            print("تم الخروج")
            break

        else:
            print("اختيار غير صحيح")
    except ValueError:
        print("الرجاء إدخال قيمة صحيحة")