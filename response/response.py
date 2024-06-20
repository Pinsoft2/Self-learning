from validator_collection import validators, checkers, errors

def response():
    validate(input("What's your email address?"))


def validate(s):
    try:
        if email_address := validators.email(s, allow_empty=False):
            print("Valid")
        else:
            print("Invalid")
    except errors.EmptyValueError:
        print("No Empty Value")
    except errors.InvalidEmailError:
        print("Invalid")


if __name__ == "__main__":
    response()