import random

def main():
    errors = 0
    correct = 0
    main_level = get_level()
    x = 0
    while x < 10:
        num1 = generate_integer(main_level)
        num2 = generate_integer(main_level)
        while 1 == 1:
            try:
                answer = int(input(f"{num1} + {num2} = "))
                if answer == num1 + num2:
                    errors = 0
                    correct += 1
                    break
                else:
                    errors += 1
                    print("EEE")
                    if errors == 3:
                        print(f"{num1} + {num2} = {num1 + num2}")
                        errors = 0
                        break
            except ValueError:
                errors += 1
                print("EEE")
                if errors == 3:
                    print(f"{num1} + {num2} = {num1 + num2}")
                    errors = 0
                    break
                pass
        x += 1
    print(f"Score: {correct}")


def get_level():
    level = input("Level: ")
    match level:
        case "1":
            return 1
        case "2":
            return 2
        case "3":
            return 3
        case other:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()