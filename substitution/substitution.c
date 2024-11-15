#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

string decipher(string key);

int main(int argc, string argv [])
{
    if (argc !=2){
        printf("Incorrect Input\n");
        return 1;
    }

    string key = argv[1];
    if (strlen(key) != 26){
        printf("Please include value 26 char keys\n");
        return 1;
    }

    for (int i=0; i < strlen(key); i++ ){
        if (!isalpha(key[i])){
            printf("Please type in alphabet characters\n");
            return 1;}
        for (int n= i+1; n < 26; n++){
            if (key[i] == key[n]){
                printf("Please only contain unique characters in the key\n");
                return 1;
            }
        }}

    string answer = decipher(key);

    printf("ciphertext: %s\n", answer);
    free(answer);
    return 0;

}

string decipher(string key)
{
    string plaintext = get_string("plaintext: ");
    int len = strlen(plaintext);
    char* ciphertext = malloc(len + 1);  // +1 for null terminator

    for (int i = 0; i < len; i++) {
        if (isalpha(plaintext[i])) {
            int index = tolower(plaintext[i]) - 'a';
            ciphertext[i] = isupper(plaintext[i]) ? toupper(key[index]) : tolower(key[index]);
        } else {
            ciphertext[i] = plaintext[i];
        }
    }
    ciphertext[len] = '\0';  // Null-terminate the string

    return ciphertext;
}
