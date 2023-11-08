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
