import random

# Generate a random lucky number between 1 and 50
lucky_number = random.randint(1, 50)

print("Welcome to the Guessing Game!")
print("I have chosen a lucky number between 1 and 50. Can you guess it?")

# Loop until the user guesses correctly
while True:
    try:
        # Get user input and convert to integer
        guess = int(input("Enter your guess: "))
        
        # Check the user's guess against the lucky number
        if guess < lucky_number:
            print("Too low! Try a higher number.")
        elif guess > lucky_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed it! The lucky number was {lucky_number}.")
            break  # Exit the loop since the user won
            
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")
