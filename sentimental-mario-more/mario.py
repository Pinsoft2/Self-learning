
def get_int(prompt):
    while True:
        try:
            height = int(input(prompt))
            if not ( 1 <= height <= 8 ):
                print("Invalid input.\n")
            else:
                return height
        except ValueError:
            print("Not an integer")

height = get_int("Height: ")


for i in range(1, height+1):
    # print("i=", i)
    # print("height=", height)
    space = height - i
    print(' '*space + "#"*i + '  ' + "#"*i)
