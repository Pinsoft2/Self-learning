import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError):
        jar=Jar(-1)
        jar=Jar("...")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar(5)
    jar.deposit(2)
    assert jar.size==2

    with pytest.raises(ValueError):
        jar=Jar(1)
        jar.deposit(2)
#cant deposit too many

def test_withdraw():
    with pytest.raises(ValueError):
        jar=Jar(2)
        jar.deposit(1)
        jar.withdraw(5)