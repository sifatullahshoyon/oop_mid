class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled


class StudentDatabase:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def view_students(self):
        for s in self.student_list:
            print(s.student_id, s.name, s.department, s.is_enrolled)


sd = StudentDatabase()

s1 = Student(101, "Rahim", "Management", False)
s2 = Student(102, "Karim", "CSE", True)
s3 = Student(103, "Bosir", "CSE", True)
s4 = Student(104, "Arosh Khan", "CSE", False)
s5 = Student(105, "Munna", "Management", True)
s6 = Student(106, "Arohi", "Tripoli", True)
s7 = Student(107, "Sujon Ahmed", "Tripoli", False)
s8 = Student(108, "Nazmul Hasan", "Physiology", True)

sd.add_student(s1)
sd.add_student(s2)
sd.add_student(s3)
sd.add_student(s4)
sd.add_student(s5)
sd.add_student(s6)
sd.add_student(s7)
sd.add_student(s8)



while True:
    print('\n-------- Student Managment Menu --------\n')

    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')

    option = int(input('Enter Your Choice (1-4): '))

    if option == 1:
        print("\n---------------------------------------------------------------------\n")
        sd.view_students()
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        print('Wrong Option. Choose Again\n')
