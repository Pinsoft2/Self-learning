from datetime import date
import sys
import inflect
import re
p = inflect.engine()

def main():
    birthday=check(input("Date Of Birth: "))
    today=date.today()
    print(f"{(p.number_to_words((today-birthday).days *24*60,andword='')).capitalize()} minutes")

def check(birth):
    if re.search(r"^\d{4}-\d{2}-\d{2}$",birth):
        year,month,day=birth.split("-")
        return date(int(year),int(month),int(day))
    else:
        sys.exit("incorrect format")


if __name__ == "__main__":
    main()