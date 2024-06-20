def bank():
    greeting=input("How are you doing?")
    print(value(greeting))


def value(greeting):
    greet=str.lower(greeting).replace(' ','')
    if greet[0:5]=="hello":
        return(0)
    elif greet[0]=="h":
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    bank()



