class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self): 
        pass

class Dog (Animal):
    def speak(self):
        print("Woof! Woof!")
    
dog = Dog("Buddy")
print(dog.name)
dog.speak()