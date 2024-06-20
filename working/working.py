import re
import sys


def work():
    print(convert(input("Hours: ")))


def convert(s):
            s=s.strip()
            mat=re.search(r"((\d\d?)(:(\d\d?))?) (AM|PM) to ((\d\d?)(:(\d\d?))?) (AM|PM)",s)
            if mat:
                if int(mat.groups()[1])>12 or int(mat.groups()[6])>12:
                    raise ValueError
                if  (mat.groups()[3]!=None and int(mat.groups()[3])>=60) or (mat.groups()[8]!=None and int(mat.groups()[8])>=60):
                    raise ValueError

# time to convert
                newtime1=int(mat.groups()[1])
                newtime2=int(mat.groups()[6])
                newmin1= mat.groups()[2]
                newmin2=mat.groups()[7]
                if mat.groups()[4]=="PM":
                    if newtime1<12:
                        newtime1+=12
                if mat.groups()[9]=="PM":
                    if newtime2<12:
                        newtime2+=12
                if mat.groups()[2]==None:
                    newmin1=':00'
                if mat.groups()[7]==None:
                    newmin2=':00'
                if mat.groups()[4]=="AM":
                    if newtime1==12:
                        newtime1=0
                if mat.groups()[9]=="AM":
                    if newtime2==12:
                        newtime2=0
                return f"{newtime1:02}{newmin1} to {newtime2:02}{newmin2}"
            else:
                raise ValueError

if __name__ == "__main__":
    work()