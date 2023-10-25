class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating objects of the derived classes
fido = Dog("Fido")
whiskers = Cat("Whiskers")

print(fido.speak())
print(whiskers.speak())
