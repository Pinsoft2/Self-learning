<<<<<<< HEAD
countofHead = 0
countofTail = 0

if not FileExistsError():
    with open('results.txt','x') as file:
        file.write("")

while True:
    result = input("Throw the coin and enter head or tail here? ").strip().lower()
    match result:
        case "head":
            countofHead += 1
            with open('results.txt','r') as file:
                results = file.readlines()
            results.append("head\n")

            with open('results.txt','w') as file:
                file.writelines(results)
            print(f"Heads: {round(countofHead/(countofHead+countofTail)*100,2)}%")


        case "tail":
            countofTail += 1
            with open('results.txt','r') as file:
                results = file.readlines()
            results.append("tail\n")

            with open('results.txt','w') as file:
                file.writelines(results)
            print(f"Heads: {round(countofHead/(countofHead+countofTail)*100,2)}%")
=======
countofHead = 0
countofTail = 0

if not FileExistsError():
    with open('results.txt','x') as file:
        file.write("")

while True:
    result = input("Throw the coin and enter head or tail here? ").strip().lower()
    match result:
        case "head":
            countofHead += 1
            with open('results.txt','r') as file:
                results = file.readlines()
            results.append("head\n")

            with open('results.txt','w') as file:
                file.writelines(results)
            print(f"Heads: {round(countofHead/(countofHead+countofTail)*100,2)}%")


        case "tail":
            countofTail += 1
            with open('results.txt','r') as file:
                results = file.readlines()
            results.append("tail\n")

            with open('results.txt','w') as file:
                file.writelines(results)
            print(f"Heads: {round(countofHead/(countofHead+countofTail)*100,2)}%")
>>>>>>> 6e4bf84439071a9e5da8dfa05fa0d27d65a1666a
