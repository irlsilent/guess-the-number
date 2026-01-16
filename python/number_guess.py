import random


print("Hi! Welcome to the Number Guessing Game\nYou have 7 chances to guess the correct number. Let's start!")

#Takes in input from the user and transforms them into Integers.
low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))

#Checks if the Lower bound is higher or equal to the Upper bound
while low >= high:
    print("Your lower bound is equal or higher than the upper bound. Please change your lower bound.")
    low = int(input("Enter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))
    
print(f"\nYou have 7 chances to guess a number between {low} and {high}. Let's get started!")


random_number = random.randint(low, high)
chances = 7
#Limits the amount of chances for the user. Can change later to scale with range size.
guess_counter = 0

#Main loop logic. Will loop until the guess counter is equal to chances or if the right number was found.
while guess_counter < chances:
    #Check to see if User input was a number and inside the range of the bounds.
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            while user_guess > high or user_guess < low:
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
        print(f"Oh no! You have used all of your {chances} chances. Too bad!")

