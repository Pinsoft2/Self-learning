answer=input("What is answer to Great Question of Life, the Universe and Everything?")
answer=str.lower(answer).replace(' ','')

match answer:
    case "42"| "forty-two"|"forty\two":
        print("Yes")
    case _:
        print("No")