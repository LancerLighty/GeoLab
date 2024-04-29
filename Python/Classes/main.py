class Student:
    def __init__(self, firstName, lastName, age):
        self.firstname = firstName
        self.lastname = lastName
        self.age = age

    def get_info(self):
        print(f"{self.firstname} {self.lastname}")

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    def remove_student(self, studentIndex):
        self.pop(studentIndex)
    def show_students(self):
        return [student.get_info() for student in self.students]

school = School("afxazetis skola", "ragaca ragaca")
student1 = Student("Tekle", "Mamporia", 16)
student2 = Student("Salome","Vigacashvili", 17)
student3 = Student("Nikoloz", "Ragacisshvili", 15)
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.show_students()