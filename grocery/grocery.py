grocerylist={}
while True:
    try:
        item=input().upper()
        newlist={item:1}
        if item in grocerylist:
            grocerylist[item]+=1
        if item not in grocerylist:
            grocerylist.update(newlist)
    except EOFError:
        print("\n")
        sortedkeys=sorted(grocerylist)
        for i in sortedkeys:
            print(grocerylist[i],i)
        grocerylist={}
        break
    except KeyError:
        pass