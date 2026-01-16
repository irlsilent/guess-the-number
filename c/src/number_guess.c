#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hi! Welcome to the Number Guessing Game\nYou have 7 chances to guess the correct number. Let's start! \n");

    int low, high, random_number, guess_counter=0, guess;
    int chances = 7;

    // Ask the user to type a number
    printf("Enter your lower bound: \n");
    scanf("%d", &low);

    printf("Enter your higher bound: \n");
    scanf("%d", &high);
    
    srand(time(0));
    random_number = (rand() % (high - low +1)) +low;

    printf("You have %d chances to guess a number between %d and %d. Let's get started!", chances,low,high); 

    while (guess_counter < chances) {
        guess_counter++;
        printf("Enter your guess: \n");
        scanf("%d", &guess);
        if (random_number > guess) {
            printf("Your guess is too high! Try again \n");
            printf("You have %d guesses left.", chances-guess_counter);
        }
        else if (random_number < guess) {
            printf("Your guess is too low! Try again \n");
            printf("You have %d guesses left.", chances-guess_counter);
        }
        else {
            printf("Congratulations! You guessed the number in %d guesses.", guess_counter);
            break;
        }

    }
    if (chances == guess_counter) {
        printf("Oh no! You have used all your guesses. Better luck next time!");
    }
    return 0;
}
