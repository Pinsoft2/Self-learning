from cs50 import get_string

number = get_string("Number: ")
num = int(number)
length = len(number)

def legit(number):
    total_sum = 0
    digits = list(number)
    length = len(number)

    # Starting from the rightmost digit (working right to left)
    for i in range(length-1, -1, -1):  # Count backwards from last digit
        digit = int(digits[i])

        # Every other digit starting from second-to-last
        if (length - i) % 2 == 0:
            # Double the digit
            doubled = digit * 2
            # If doubled digit is > 9, sum its digits (or subtract 9, same result)
            if doubled > 9:
                doubled -= 9
            total_sum += doubled
        else:
            total_sum += digit

    if total_sum % 10 != 0:
        print("INVALID")
        return 1
    else:
        return 0


if legit(number) == 0 :
    if len(number) == 15:
        if int(number[:2]) == 34 or int(number[:2]) == 37:
            print ("AMEX")
        else:
            print("INVALID")
    elif len(number) == 16:
        if int(number[:2]) in [51,55]:
            print ("MASTERCARD")
        if int(number[0]) == 4:
            print ("VISA")
        else:
            print("INVALID")
    elif len(number) == 13 and int(number[0]) == 4:
        print ("VISA")
    else:
        print("INVALID")
