import re
import sys


def youtube():
    print(parse(input("HTML: ")))


def parse(s):
    s=s.replace("<","").replace(">","")
    if url:=re.search(r'.+src=\"(https?)://(www.)?youtube.com/embed/(\w+)\"( title)?.+$',s):
        return f"https://youtu.be/{url.group(3)}"
    else:
        return None

if __name__ == "__main__":
    youtube()