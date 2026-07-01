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


students = [
    (101, "Rahim", "Management", False),
    (102, "Karim", "CSE", True),
    (103, "Bosir", "CSE", True),
    (104, "Arosh Khan", "CSE", False),
    (105, "Munna", "Management", True),
    (106, "Arohi", "Tripoli", True),
    (107, "Sujon Ahmed", "Tripoli", False),
    (108, "Nazmul Hasan", "Physiology", True)
]

sd = StudentDatabase()

for s in students:
    student_obj = Student(*s)
    sd.add_student(student_obj)



while True:
    print('\n-------- Student Managment Menu --------\n')

    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')

    option = int(input('Enter Your Choice (1-4): '))

    if option == 1:
        print('\n-------- View All Students --------\n')
        sd.view_students()
    elif option == 2:
        print('\n-------- Enroll Student --------\n')
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        print('Wrong Option. Choose Again\n')
