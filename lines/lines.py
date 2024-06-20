import sys

while True:
    try:
        if len(sys.argv)<2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[-1].endswith("py")==False:
            sys.exit("Not a python file")
        else:
            num_lines=0
            linesnew=[]
            with open(sys.argv[-1])as file:
                for line in file:
                    lines = line.strip().split("\n")
                    linesnew.append(lines)
            for codes in linesnew:
                if codes[0]!="" and codes[0][0]!="#":
                    num_lines += 1
            print(num_lines)
            break
    except FileNotFoundError:
        pass

