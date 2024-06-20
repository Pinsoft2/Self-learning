import random
import sys

def main():
    level = get_level()
    p = 0
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = int(x+y)
        guess = int(input(f"{x} + {y} = "))
        if guess == answer :
            score += 1
        while guess != answer :
            p += 1
            print("EEE")
            guess = int(input(f"{x} + {y} = "))
            if p == 2:
                print(f"{x} + {y} = {answer}")
                p = 0
                break
    print(score)
    sys.exit(0)

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError: # just catch the exceptions you know!
            pass

def generate_integer(level):
    if level==1:
        number=random.choice(range(0,10))
    if level==2:
        number=random.choice(range(10,100))
    if level==3:
        number=random.choice(range(100,1000))
    return number


if __name__ == "__main__":
    main()



