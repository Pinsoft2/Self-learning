import pytest
from plates import is_valid

def test_punc():
    assert is_valid(",.?")==False
    assert is_valid("WOW,YEY")==False
    assert is_valid("HELLO WORLD")==False
    assert is_valid(".CS50")==False
    assert is_valid("CS 50")==False
    assert is_valid("CS,590")==False
    assert is_valid("CS.500")==False

def test_length():
    assert is_valid("MLAAA000")==False
    assert is_valid("Y")==False

def test_normal():
    assert is_valid("AAA222")==True
    assert is_valid("CANN021")==False
    assert is_valid("CS50")==True

def test_zero():
    assert is_valid("0WW33")==False
    assert is_valid("CS05")==False

def test_last():
    assert is_valid("CS50P")==False

def test_alltext():
    assert is_valid("TEXTO")==True
    assert is_valid("010191")==False
    assert is_valid("T2209")==False


def test_first():
    assert is_valid("N9981")==False

def test_numeric():
    assert is_valid("TT209")==True
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("A")==False
    assert is_valid(",A")==False
    assert is_valid("$1") == False
    assert is_valid("1$") == False
    assert is_valid("12$") == False
    assert is_valid("  AB") == False
    assert is_valid("!?AB2*") == False
    assert is_valid("*:") == False
    assert is_valid("B>") == False


def test_numberOfCharacters():
    assert is_valid("A")==False
    assert is_valid("AA")==True
    assert is_valid("AAA")==True
    assert is_valid("AA2")==True
    assert is_valid("AAAA")==True
    assert is_valid("...")==False
    assert is_valid("11112")==False
    assert is_valid("     ")==False
    assert is_valid(",, 11")==False

def test_alphanumeric():
    assert is_valid(" A110")==False
    assert is_valid(",,50")==False
    assert is_valid("1A50")==False
    assert is_valid("AA")==True
    assert is_valid("A2")==False
    assert is_valid("2A")==False
    assert is_valid("22")==False

#assert is_valid("")