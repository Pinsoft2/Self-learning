import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    #find matches
    if mat:=re.findall(r"(\bum\b)",s,re.IGNORECASE):
        return len(mat)
    else:
        raise ValueError
        sys.exit(0)

if __name__ == "__main__":
    main()