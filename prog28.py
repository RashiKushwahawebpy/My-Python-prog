#10. Matching Classes / Objects
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
student = Student("Aman", 90) 
match student:
    case Student(name=name, marks=marks):
        print(name, marks)