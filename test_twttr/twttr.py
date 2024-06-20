# input=input("Input:")
# for letters in input:
#     if letters == "A" or letters == "E" or letters == "I" or letters == "O" or letters == "U" or letters == "a" or letters == "e" or letters == "i" or letters == "u" or letters == "o" :
#         letters=""
#     print(letters,end="")
import sys

def twttr():
    userInput=input("Input:")
    print(shorten(userInput))

def shorten(word):
    newWord=""
    for letters in word:
        if letters not in ["a","e","i","o","u","A","E","I","O","U"]:
            newWord=newWord+letters
    return(newWord)

if __name__ == "__main__":
    twttr()