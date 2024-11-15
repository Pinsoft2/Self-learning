#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long number;
    do {
        number = get_long("Credit card number: ");
    }
    while (number<0);

    long original = number;
    int count = 1;
    int sum1 = 0;
    int sum2 = 0;
    int digit;

    while (number > 0) {
        digit = number % 10;  // Get the last digit
        // printf("%d(%i) ", digit, count);     // Print the digit

        if (count%2 == 0){
            int new_d1;
            if (digit>=5){
                new_d1 = ((digit * 2) % 10) + 1;}
            else {new_d1 = digit*2;}

        sum1 = sum1 + new_d1;}

        else {sum2 += digit;}

        count ++;
        number = number / 10;}

    int total = sum1+sum2;
    count = count -1;


    if (total % 10 == 0) {
        long first_two_digits = original;
        while (first_two_digits >= 100) {
            first_two_digits /= 10;
        }
        // printf("first2: %li\n", first_two_digits);
        if ((first_two_digits==34||first_two_digits==37) && count ==15){
            printf("AMEX\n");}
        else if (digit == 4 && (count == 13||count == 16)){
            printf("VISA\n");}
        else if (first_two_digits >= 51 && first_two_digits <= 55 && count ==16){
            printf("MASTERCARD\n");}
        else {
            printf("INVALID\n");}
    }
    else {printf("INVALID\n");}
}