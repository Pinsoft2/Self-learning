camel=input("camelCase:")
for letters in camel:
    if letters.isupper()==True:
        letters="_"+letters.lower()
    print(str(letters),end="")