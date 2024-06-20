from numb3rs import validate
import pytest
import re
import sys

def test_less_dots():
    assert validate("512.512.512.512")==False
    assert validate("1.2.3.1000")==False
    assert validate("255.255.255.255")==True

def test_first_byte():
    assert validate("1.255.255.255")==True
    assert validate("266.255.255.255")==False
    assert validate("2.300.300.300")==False

def test_normal_case():
    assert validate("cat")==False