from fuel import convert, gauge
import pytest

def test_correctReturn():
    assert convert("3/3")==100
    assert convert("3/4")==75
    assert convert("1/2")==50

def test_gauge():
    assert gauge(1)=="E"
    assert gauge(50)=="50%"
    assert gauge(99)=="F"


def test_largerThanOne():
    with pytest.raises(ValueError):
        convert("Hi/WOW")
        convert("4/3")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
        convert("0/0")
