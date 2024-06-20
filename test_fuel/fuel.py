def fuel():
    fraction=input("Fraction:")
    print(gauge(convert(fraction)))

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
            raise

def gauge(percentage):
    if percentage <=1:
        return("E")
    elif 100>=percentage >=99:
        return("F")
    elif 1<percentage<99:
        return(f"{percentage/100:.0%}")

if __name__ == "__main__":
    fuel()


