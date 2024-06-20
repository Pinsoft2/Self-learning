import sys
wholeName=[]

while True:
    try:
        name=input("Name:")
        wholeName.append(name)
    except EOFError:
        if len(wholeName)>2:
            wholeName[-1]="and "+wholeName[-1]
            wholeName=', '.join(wholeName)
        if len(wholeName)==1:
            wholeName=''.join(wholeName)
        if len(wholeName)==2:
            wholeName[1]="and "+wholeName[1]
            wholeName=' '.join(wholeName)
        print("Adieu, adieu, to",wholeName)
        sys.exit()