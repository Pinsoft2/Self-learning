def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
#all characters?
    for _ in s:
        if _.isdigit()==False and _.isalpha()==False:
            return False
#mixed?
    text=""
    numbers=""
    if len(s)>1 and s[1].isdigit()==True:
        return False
    for i in s:
        if(i.isdigit()):
            numbers+=i
        else:
            text+=i
    res=text+numbers
    for f in s:
        if f.isdigit()==True:
            break
    if res !=s:
        return False
    elif len(s)==1:
        return False
    elif isinstance(s[0],str) and isinstance(s[1],str) and 2<=len(s)<=6 and f!="0":
        return True
    else:
        return False

if __name__ == "__main__":
    main()