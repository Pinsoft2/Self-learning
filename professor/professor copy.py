import random
import sys

def main():
    level=get_level()
    p=0
    score=0
    for i in range(10):
        x,y=generate_integer(level)
        answer=int(x+y)
        while True:
            try:
                guess=int(input(f"{x} + {y} = "))
                if guess==answer:
                    i=i+1
                    score+=1
                    break
                if guess!=answer:
                    p+=1
                    print("EEE")
                    if p==3:
                        print(f"{x} + {y} = {answer}")
                        p=0
                        i=i+1
                        break
            except ValueError:
                pass

    print(score)
    sys.exit(0)


def get_level():
    while True:
        try:
            level=int(input("Level: "))
        except ValueError: # just catch the exceptions you know!
            pass
        else:
            if 1 <= level <= 3: # this is faster
                return level
                break
            else:
                pass


def generate_integer(level):
    x=0
    y=0
    if level==1:
        x=random.choice(range(0,9))
        y=random.choice(range(0,9))
    if level==2:
        x=random.choice(range(10,100))
        y=random.choice(range(10,100))
    if level==3:
        x=random.choice(range(100,1000))
        y=random.choice(range(100,1000))
    return x,y

if __name__ == "__main__":
    main()



