calendar={
        "January":"01",
        "February":"02",
        "March":"03",
        "April":"04",
        "May":"05",
        "June":"06",
        "July":"07",
        "August":"08",
        "September":"09",
        "October":"10",
        "November":"11",
        "December":"12"}
while True:
    try:
        originalDate=input("Date:").strip()
        if originalDate[0].isdigit()==True:
            if "," in originalDate:
                pass
            else:
                month,day,year=originalDate.split("/")
                if 1<=int(day)<=31 and 1<=int(month)<=12:
                    print(year,"-","%02d" %(int(month)),"-","%02d" %(int(day)),sep="")
                    break
                else:
                    pass
        if originalDate[0].isalpha()==True:
            if "/" in originalDate or "," not in originalDate:
                pass
            else:
                month,day,year=originalDate.replace(",","").split(" ")
                if 1<=int(day)<=31:
                    print(year,"-",calendar[month],"-","%02d" %(int(day)),sep="")
                    break
                else:
                    pass
    except KeyError:
        pass