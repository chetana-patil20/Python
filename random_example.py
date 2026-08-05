#Random module in python is used to generate random numbers. It can be used to generate random integers, floating point numbers, and even random selections from a list.

#for printing all list of random module functions
# import random
# print(help(random))

import random
# number = random.randint(1,6)#generating random integer between 1 and 6
# print(number)

# low = 1
# high = 100
# num = random.randint(low,high)#generating random integer between low and high
# print(num)

# number = random.random()#generating random float between 0 and 1
# print(number)

#rock,paper,scissors game
# options = ("rock","paper","scissors")
# option = random.choice(options)#generating random choice from options
# print(option)

#Shuffle method for cards 
# cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
# random.shuffle(cards)
# print(cards)

#Guess the number game
low = 1
high = 100
guesses = 0
number = random.randint(low,high)
while True:
    guess = int(input(f"Guess a number between {low} and {high}: "))
    guesses += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} in {guesses} guesses.")
        break
    print(f"You have made {guesses} guesses so far.")