def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
print("Fibonacci Sequence:", fibonacci(num_terms))
Guess the Number Game:

python
Copy code
import random

target_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess == target_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < target_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
File I/O - Reading and Writing a File:

python
Copy code
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\nPython is awesome!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
Simple Web Scraping with BeautifulSoup:

python
Copy code
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    print("Title of the web page:", title)
else:
    print("Failed to fetch the web page.")
Basic Data Visualization with Matplotlib:

python
Copy code
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()
