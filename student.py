class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def enroll_student(self):
        if self.is_enrolled:
            print(f"Student {self.student_id} is already enrolled.")
        else:
            self.is_enrolled = True
            print(f"Student {self.student_id} enrolled successfully.")


class StudentDatabase:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def view_students(self):
        print("\n------ Student List ------")
        for s in self.student_list:
            print(
                f"ID: {s.student_id}, "
                f"Name: {s.name}, "
                f"Dept: {s.department}, "
                f"Enrolled: {s.is_enrolled}"
            )

    def find_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                return student
        return None

    def enroll_student_by_id(self, student_id):
        student = self.find_student(student_id)
        if student:
            student.enroll_student()
        else:
            print("Student not found!")


# ---------------- DATA ----------------

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
    sd.add_student(Student(*s))


# ---------------- MENU ----------------

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
        sid = int(input("Enter Student ID: "))
        sd.enroll_student_by_id(sid)
    elif option == 3:
        pass
    else:
        print("Exiting program...")
        break