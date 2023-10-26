class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects of the Person class
alice = Person("Alice", 30)
bob = Person("Bob", 25)

alice.greet()
bob.greet()
