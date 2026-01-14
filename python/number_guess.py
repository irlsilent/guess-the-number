import random

print("Hi! Welcome to the Number Guessing Game\n You have 7 chances to guess the correct number. Let's start!")

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))

print(f"\n You have 7 chance to guess a number between {low} and {high}. Let's get started!")

random_number = random.randint(low, high)
chances = 7
guess_counter = 0

while guess_counter < chances:
    user_guess = int(input("Enter your guess: "))
    guess_counter += 1
    
    if (user_guess < random_number):
        {
            exit
        }
    elif (user_guess > random_number):
        {
            exit
        }
    else:
        {
            exit
        }
        
if (guess_counter == chances):
    {
        print(f"Oh no! You have used all of your {chances} chances. Too bad!")
    }