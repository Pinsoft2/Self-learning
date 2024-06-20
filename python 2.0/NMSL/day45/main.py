class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        name = self.name.upper()
        print(name)
        return name

    def age(self, current_year):
        result = current_year - self.birthyear
        print(result)
        return result


user = User("John",1999)
user.age(current_year=2023)
user.get_name()
