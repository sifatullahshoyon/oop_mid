class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def enroll_student(self):
        if self.is_enrolled:
            print(f"Error: Student {self.student_id} is already enrolled.")
        else:
            self.is_enrolled = True
            print(f"Student {self.student_id} enrolled successfully.")

    def drop_student(self):
        if not self.is_enrolled:
            print(f"Error: Student {self.student_id} is not enrolled.")
        else:
            self.is_enrolled = False
            print(f"Student {self.student_id} dropped successfully.")


class StudentDatabase:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def find_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                return student
        return None

    def enroll_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            print("Error: Invalid Student ID.")
            return

        student.enroll_student()

    def drop_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            print("Error: Invalid Student ID.")
            return

        student.drop_student()

    def view_students(self):
        print("\n---------------- Student List ----------------")

        for student in self.student_list:
            print(
                f"ID: {student.student_id}, "
                f"Name: {student.name}, "
                f"Department: {student.department}, "
                f"Enrolled: {student.is_enrolled}"
            )


# ---------------- Data ----------------

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

for student_data in students:
    student = Student(*student_data)
    sd.add_student(student)


# ---------------- Menu ----------------

while True:
    print("\n-------- Student Management Menu --------\n")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")


    option = int(input("Enter Your Choice (1-4): "))

    if option == 1:
        sd.view_students()

    elif option == 2:
        print("\n---------------- Enroll Student ----------------\n")
        student_id = int(input("Enter Student ID: "))
        sd.enroll_student(student_id)
          
    elif option == 3:
        print("\n---------------- Drop Student ----------------\n")
        student_id = int(input("Enter Student ID: "))
        sd.drop_student(student_id)

    elif option == 4:
        print("Exiting program...")
        break

    else:
        print("Error: Please choose a number between 1 and 4.")

   

