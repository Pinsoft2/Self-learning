#q1
while True:
    try:
        denom = float(input("Enter total value: "))
        nom = float(input("Enter value: "))
    
    except ZeroDivisionError:
        print("Your total value cannot be zero.")
    except ValueError:
        print("You need to enter a number. Run the program again.")

