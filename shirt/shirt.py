import sys
import PIL
from PIL import Image

while True:
    try:
        if len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].lower().endswith("jpg")==False and sys.argv[1].lower().endswith("jpeg")==False and sys.argv[1].lower().endswith("png")==False:
            sys.exit("Invalid Output")
        elif sys.argv[1].lower()[-3:-1]!=sys.argv[2].lower()[-3:-1]:
            sys.exit("Input and output have different extensions")
        else:
            shirt = Image.open("shirt.png")
            with Image.open(sys.argv[1]) as before:
                before=PIL.ImageOps.fit(before, size=shirt.size, method=PIL.Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
                before.paste(shirt,shirt)
                before.save(sys.argv[2])
            break
    except FileNotFoundError:
        sys.exit("Input does not exist")