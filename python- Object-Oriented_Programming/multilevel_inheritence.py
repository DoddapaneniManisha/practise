class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Poodle(Dog):
    def speak(self):
        return "Bark!"

animal = Animal()
dog = Dog()
poodle = Poodle()

print(animal.speak())
print(dog.speak())
print(poodle.speak())
