def fuel():
    fraction=input("Fractiion:")
    gauge(convert(fraction))

def convert(fraction):
    while True:
        try:
            x,y=fraction.split("/")
            if x<=y:
                percentage=round(int(x)/int(y)*100)
                return percentage
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if percentage <=1:
        print("E")
    elif 100>=percentage >=99:
        print("F")
    elif 1<percentage<99:
        print(percentage,"%",sep="")

if __name__ == "__main__":
    fuel()


