import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100. Try to guess it.")

attempts = 0

while True:
    # Get a guess from the player
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")

print("Thank you for playing!")
