class Vehicle:
    def start_engine(self):
        return "Engine started."

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

class Motorcycle(Vehicle):
    pass

# Creating objects of the derived classes
car = Car()
motorcycle = Motorcycle()

print(car.start_engine())       # Calls Car's overridden method
print(motorcycle.start_engine()) # Inherits the method from Vehicle
