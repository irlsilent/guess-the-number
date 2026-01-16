#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hi! Welcome to the Number Guessing Game\nYou have 7 chances to guess the correct number. Let's start! \n");
    // Create an integer variable that will store the number we get from the user
    int low, high, random_number, guesses;
    int chances = 7;

    // Ask the user to type a number
    printf("Enter your lower bound: \n");
    scanf("%d", &low);

    printf("Enter your higher bound: \n");
    scanf("%d", &high);
    
    srand(time(0));
    random_number = (rand() % (high - low +1)) +low;

    printf("You have %d chances to guess a number between %d and %d. Let's get started!", chances,low,high); 

    while (guesses < chances) {
        guesses++;
    }
    return 0;
}
