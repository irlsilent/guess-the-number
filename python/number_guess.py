import random

print("Hi! Welcome to the Number Guessing Game\nYou have 7 chances to guess the correct number. Let's start!")

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))

while low >= high:
    print("Your lower bound is equal or higher than the upper bound. Please change your lower bound.")
    low = int(input("Enter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))
    
print(f"\nYou have 7 chance to guess a number between {low} and {high}. Let's get started!")

random_number = random.randint(low, high)
chances = 7
guess_counter = 0

while guess_counter < chances:
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            while user_guess > high:
                print("Your guess is out of bounds.")
                user_guess = int(input("Enter your guess: "))
            break
        except ValueError:
            print("That is not a number. Try again!")  
    guess_counter += 1
    
    if (user_guess < random_number):
            print(f"You are too low!\nYou have {chances-guess_counter} chances left!")
    elif (user_guess > random_number):
            print(f"You are too high!\nYou have {chances-guess_counter} chances left!")
    else:
            print(f"Congratulations! You guessed the correct number in {guess_counter} guesses!")
            break
        
if (guess_counter == chances):
    {
        print(f"Oh no! You have used all of your {chances} chances. Too bad!")
    }

