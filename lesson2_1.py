class User:
    __password = "abc@123"

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username

    def getPassword(self):
        return self.__password
    
    def setPassword(self):
        old_password = input("Enter your old password : ")
        if old_password == self.__password : 
            new_password = input("Enter your new password : ")
            self.__password = new_password
        else : 
            print("Please Enter the correct password")

class Car :
    def __init__ (self, brand, model, fuel, color):
        self.brand = brand
        self.model = model
        self.fuel = fuel 
        self.color = color

    def getColor(self):
        return self.color
    
    def setColor(self): 
        self.color = newcolor

    def showCar(self):
        print(f"Car - {self.brand} - {self.model}, Fuel Type - {self.fuel}, color - {self.color}")

class SUV(Car): 
    def __init__(self, brand, model, fuel, color, transmission, turbo): 
        Car.__init(self, brand, model, fuel, color)
        self.tranmission = transmission
        self.turbo = turbo

    def showCar(self):
        print(
            "Car - {} - {}, Fuel Type - {}, Color - {}, Transmission - {}, Turbo True/False - {}".format(
                self.brand, 
                self.model, 
                self.fuel, 
                self.color, 
                self.transmission, 
                self.turbo
                )
        )