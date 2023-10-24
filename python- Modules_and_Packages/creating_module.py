# mymodule.py
def greeting(name):
    return f"Hello, {name}!"

# main.py
import mymodule

message = mymodule.greeting("Alice")
print(message)
