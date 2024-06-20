from bank import value
import pytest


def test_hello():
    assert value("hello")==0


def test_randomstring():
    assert value("asjaisu")==100
    assert value("AISOIAMXOO")==100

def test_Hsomething():
    assert value("Hey")==20