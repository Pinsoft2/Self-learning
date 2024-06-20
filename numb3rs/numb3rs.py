import re
import sys

def numbers():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    while True:
        try:
            match=re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip)
            if 0<=int(match.group(1))<=255 and 0<=int(match.group(2))<=255 and 0<=int(match.group(3))<=255 and 0<=int(match.group(4))<=255:
                return True
            else:
                return False
        except (AttributeError, ValueError):
            return False

if __name__ == "__main__":
    numbers()