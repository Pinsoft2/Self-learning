class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError("Invalid capacity")
        self.capacity=capacity
        self.size=0

        #If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

    def __str__(self):
        return("🍪"*self.size)
#__str__ should return a str with 🍪, where is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

#withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
#size should return the number of cookies actually in the cookie jar.

    @size.setter
    def size(self,size):
        self._size = size

    def deposit(self, n):
        size = self.size + n
        if size> self.capacity:
            raise ValueError("exceed capacity")
        self.size=size
        return self.size
#deposit should add n cookies to the cookie jar.
# If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.

    def withdraw(self, n):
        size = self.size - n
        if size<0:
            raise ValueError("no more cookies")
        self.size=size
        return self.size

jartest=Jar(10)
jartest.deposit(3)
jartest.withdraw(1)
print(jartest)