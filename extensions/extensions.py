file=input("enter file's name thx <3").lower().replace(" ",'')
# print('image/'+("cs50.gif")[-3:])
if file[-4:]=='jpeg' or file[-3:]=='jpg':
     print("image/jpeg")
else:
    match file[-3:]:
        case "gif"|"png":
            print("image/"+file[-3:])
        case "txt":
            print("text/plain")
        case "zip"|"pdf":
            print("application/"+file[-3:])
        case _:
            print("application/octet-stream")