class StudentDatabase:
    # def __init__(self, student_id, name, department, is_enrolled) -> None:
    #     self.student_id = student_id
    #     self.name = name
    #     self.department = department
    #     self.enroll = is_enrolled

    def __init__(self):
        self.student_list = []

    def add_student(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.enroll = is_enrolled

class Student(StudentDatabase):
    def __init__(self):
        super().__init__()

rahim = StudentDatabase(101, 'Rahim', 'Management', False)
rahim.add_student(101, 'Rahim', 'Management', False)   

while True:
    print('\n-------- Student Managment Menu --------\n')

    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')

    option = int(input('Enter Your Choice (1-4): '))

    if option == 1:
        print("\n---------------------------------------------------------------------\n")
        rahim.add_student()
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        print('Wrong Option. Choose Again\n')
