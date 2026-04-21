class Student : 
    fruit_count = 0
    
    def __init__(self, name, school_name, grade) : 
        self.name = name
        self.school_name = school_name
        self.grade = grade

    def get_grade(self) : 
        return self.grade
    
    def set_grade(self, new_grade) : 
        self.grade = new_grade

    def showDetails(self):
        print("I am {}, from {}, in grade {}.".format(self.name, self.school_name , self.grade, ))

Bob = Student("Bob", "Bob primary school","5")
Bob.showDetails()

print("Grade of ", Bob.name, ":", Bob.get_grade)
Bob.set_grade("6")
Bob.showDetails()

Paul = Student("Paul", "paul school", "2")
Paul.showDetails()

