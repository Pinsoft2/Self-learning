import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

# if originalText.isdigit()==False:
if len(sys.argv)==3:
    if (sys.argv[1]=="-f" or sys.argv[1]=="--font" )and sys.argv[2] in figlet.getFonts():
        originalText=input("Input:")
        figlet.setFont(font=str(sys.argv[2]))
        print("Output:", figlet.renderText(originalText))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv)==1:
    randomFont=str(random.choice(figlet.getFonts()))
    print(randomFont)
    figlet.setFont(font=randomFont)
    originalText=input("Input:")
    print("Output:", figlet.renderText(originalText))
else:
    sys.exit("Invalid usage")