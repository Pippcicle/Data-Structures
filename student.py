class Student :
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

    def get_marks(self) : 
        return self.marks

    def set_marks(self, new_marks) : 
        self.marks = new_marks

name = input("Enter Student Name : ")
marks = int(input("Enter Student Marks : "))

student1 = Student(name, marks)

print("Current Marks : ", student1.get_marks())

new_marks = int(input("Enter Updated Marks : "))
student1.set_marks(new_marks)

print("Updated Marks : ", student1.get_marks())
