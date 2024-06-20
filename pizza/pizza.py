import sys
from tabulate import tabulate
import csv

while True:
    try:
        if len(sys.argv)<2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[-1].endswith("csv")==False:
            sys.exit("Not a CSV file")
        else:
            menu=[]
            with open(sys.argv[-1]) as file:
                excel = csv.DictReader(file)
                menu=list(excel)
                # for row in excel:
                #     menu.append({"Sicilian Pizza type": list(menu)[0],"Small":list(menu)[1], "Large":list(menu)[2]})
            print(tabulate(menu, headers="keys", tablefmt="grid"))
            break
# >>> print(tabulate(table, headers, tablefmt="outline"))
    except FileNotFoundError:
        sys.exit("File does not exist")

            # dict_from_csv = dict(list(excel)[0])
            # list_of_column_names = list(dict_from_csv.keys())