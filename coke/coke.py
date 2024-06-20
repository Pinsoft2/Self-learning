amount_due=50
while amount_due>0:
    insert=int(input("Insert coin:"))
    if insert==25 or insert==10 or insert==5:
        amount_due=amount_due-insert
        if amount_due >0:
            print("Amount Due:",amount_due)
    else: print("Amount Due:",amount_due)
print("Change Owed: ",amount_due*-1,sep="")
#refresh