// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose number of buckets in hash table
const unsigned int N = 10000;  // Increased from 26 for better distribution

// Hash table
node *table[N];

// Track number of words in dictionary
unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Create a temporary array to store lowercase version of word
    char temp[LENGTH + 1];
    int len = strlen(word);

    // Convert word to lowercase for case-insensitive comparison
    for (int i = 0; i < len; i++)
    {
        temp[i] = tolower(word[i]);
    }
    temp[len] = '\0';

    // Hash the word to get the index
    unsigned int index = hash(temp);

    // Traverse the linked list at that index
    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcmp(cursor->word, temp) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash_value = 0;

    // Loop through each character in the word
    for (int i = 0; word[i] != '\0'; i++)
    {
        // Add ASCII value of current character
        hash_value += tolower(word[i]);

        // Multiply by a prime number (31 is commonly used)
        // This helps distribute values more evenly
        hash_value = (hash_value * 31);
    }

    // Make sure the hash value fits within our table size
    return hash_value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // Create new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        // Copy word into node
        strcpy(n->word, word);

        // Hash word
        unsigned int index = hash(word);

        // Insert node into hash table
        n->next = table[index];
        table[index] = n;

        // Increment word count
        word_count++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Free linked lists
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}