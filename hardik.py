import random

# Generate a random array of numbers
array = [random.randint(1, 20) for _ in range(5)]

print("Welcome to the Array Game!")
print("Try to guess a number in the array.")

while True:
    # Get a guess from the player
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess in array:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Try again. That number is not in the array.")
