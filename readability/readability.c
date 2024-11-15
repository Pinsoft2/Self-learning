#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int get_grade(string sentence);

int main(void)
{
    string sentence = get_string("Text: ");
    int grade = get_grade(sentence);

    if (grade < 1){
        printf("Before Grade 1\n");
    }
    else if (grade >= 16){
        printf("Grade 16+\n");
    }
    else {
        printf("Grade %i\n", grade);
    }

}

int get_grade(string sentence){

    float S = 0;
    float L = 0;
    int word_count = 1;
     // get words
    for (int i = 0; i < strlen(sentence) ; i++)
         {
        // Count letters
        if (isalpha(sentence[i])){
            L++;
        }
        if (sentence[i] ==' '){
            word_count++;}
        if (sentence[i] == '.' || sentence[i] == '!'|| sentence[i] == '?'){
            S++;
        }
        }

    L = L/word_count * 100;
    S = S/word_count * 100;

    int grade = round(0.0588 * L - 0.296 * S - 15.8);
    // printf("%f L, %f S, %i words\n", L , S , word_count);
    return grade;

}