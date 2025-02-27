#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int getRandomNumber(int min, int max)
{
    int random = rand();
    random = random % (max - min + 1);
    random = random + min;

    return random;
}
int main()
{
    srand(time(NULL));
    int hiddenNumber = getRandomNumber(1, 100);
    int guess;

    printf("Guess an integer between 1 and 100: \n");
    scanf("%d", &guess);

    while (guess != hiddenNumber)
    {
        if (guess < hiddenNumber)
        {
            printf("Hmm.. nope, higher!\n");
            scanf("%d", &guess);
        }
        if (guess > hiddenNumber)
        {
            printf("Hmm.. nope, lower!\n");
            scanf("%d", &guess);
        }
    }
    printf("You did it! Your guess was correct.");
}