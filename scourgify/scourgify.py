import sys
import csv

while True:
    try:
        if len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        else:
            students=[]
            ayo=[]
            newlist=[]
            with open(sys.argv[-2]) as before:
                excel = csv.DictReader(before)
                for row in excel:
                    students.append({"name":row["name"],"house":row["house"]})
            for eachdict in students:
                last,first=eachdict['name'].split(",")
                first=first.lstrip(" ")
                ayo=[first,last,eachdict['house']]
                print(ayo)
                newlist.append(ayo)
            print(newlist)
            fields= ["first","last","house"]
            with open(sys.argv[-1],'w',newline='') as after:
                writer = csv.writer(after)
                writer.writerow(fields)
                writer.writerows(newlist)
            break
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")