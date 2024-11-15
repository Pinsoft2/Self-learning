#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int rate(char letter);

int main(void)
{
    int p1 = 0;
    int p2 = 0;
    string player_1 = get_string("Player 1: ");
    string player_2 = get_string("Player 2: ");

    for (int i = 0, n=strlen(player_1); i<n; i++)
    {
        player_1[i] = toupper(player_1[i]);
        int score = rate(player_1[i]);
        p1 += score;
        }


    for (int i = 0, n=strlen(player_2); i<n; i++)
    {
        player_2[i] = toupper(player_2[i]);
        int score = rate(player_2[i]);
        p2 += score;
    }

    if (p1 > p2){
        printf("Player 1 Wins!\n");
    }
    else if (p1 == p2){
        printf("Tie!\n");
    }
    else if (p1 < p2){
        printf("Player 2 Wins!\n");
    }

}

int rate(char letter){
    int score = 0;
    if (letter == 'A'|| letter == 'E' || letter == 'I'|| letter == 'L'|| letter == 'N'|| letter == 'O'|| letter == 'R'|| letter == 'S'|| letter == 'T'|| letter == 'U'){
        score = 1;
    }
    else if (letter == 'D'|| letter == 'G'){
        score = 2;
    }
    else  if (letter == 'B'|| letter == 'C'|| letter == 'M'|| letter == 'P'|| letter == 'I'){
        score = 3;
    }
    else if (letter == 'F'|| letter == 'H'|| letter == 'V'|| letter == 'Y'|| letter == 'W'){
        score = 4;
    }
    else if (letter == 'K'){
        score = 5;
    }
    else if (letter == 'J'|| letter == 'X'){
        score = 8;
    }
    else if (letter == 'Q'|| letter == 'Z'){
        score = 10;
    }

    return score;
}
