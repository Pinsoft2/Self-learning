def main():
    print(convert())

def convert():
    x=input("test?")
    x=x.replace(":)","🙂").replace(":(","🙁")
    return x
main()
# print(str(input("test?")).replace(":)","🙂").replace(":(","🙁"))

