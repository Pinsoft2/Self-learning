def main():
    x=input("What's the time now?")
    if x[-1]==".":
        converted_time,timeofday=convert(x)
    else: converted_time=convert(x)

    if 7<=float(converted_time)<=8 and len(x)==4:
        print("breakfast time")
    elif 12<=float(converted_time)<=13:
        print("lunch time")
    elif 18<=float(converted_time)<=19 or (6<=float(converted_time)<=7 and timeofday=="p.m."):
        print("dinner time")

def convert(time):
    if time[-1]==".":
        hours,minutes,timeofday=time.replace(" ",":").split(":")
        converted_time=float(hours)+float(minutes)/60
        return [converted_time, timeofday]
    else:
        hours,minutes=time.split(":")
        converted_time=float(hours)+float(minutes)/60
        return converted_time

main()


