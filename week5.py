
# --- Assignment 1
# Defining the parent class
class Smartphone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.battery = battery 
    
    # Method to describe the phone
    def describe_phone(self):
        print(f"{self.brand} {self.model} - Battery: {self.battery}%")

    # Method to make a call
    def call(self, contact):
        if self.battery > 5:
            print(f"Calling {contact}...")
            self.battery -= 5
        else:
            print("Battery too low to make a call.")
    # Method to charge the phone
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"Charging... Battery now at {self.battery}%")

# Child class that inherits from the parent class 
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery=100, cooling_system=True):
        # Call the parent class constructor
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    # Method to play game
    def play_game(self, game):
        if self.battery > 25:
            print(f"Playing {game} on {self.model}...")
            self.battery -= 25
        else:
            print(" Battery too low to play games.")

# An instance of the SmartPhone
phone = Smartphone("Samsung", "Z-Fold")
phone.describe_phone()
phone.call("Sammy ")
phone.charge(10)

# An instance of the gaming phone
gaming_phone = GamingPhone("Asus", "ROG Phone 9")
gaming_phone.describe_phone()
gaming_phone.play_game("WarZone")
gaming_phone.charge(30)

print()
# -- Assignment 2

# Parent class Vehicle
class Vehicle:
    #method to represent movement of the vehicle
    def move(self):
        print("The vehicle is moving...")

# defining subclass for car that inherits from class Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving car on the road...")

# defining subclass for plane that inherits from class Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying airplane in the sky...")

# defining subclass for boat that inherits from class Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing boat on the water...")


vehicles = [Car(), Plane(), Boat()]

#iterate over each vehicle in the list using for loop
for vehicle in vehicles:
    # calling the move method
    vehicle.move() 