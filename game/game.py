import sys
import random
range=[]

while True:
    try:
        rangeMax=input("Level: ")
        if isinstance(rangeMax,int)=='False' or int(rangeMax)<1:
            pass
        else:
            range=[1,rangeMax]
            answer=int(random.choice(range))
            guess=int(input("Guess: "))
            if guess<answer:
                print("Too small!")
            elif guess>answer:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
    except (ValueError,KeyError):
        pass