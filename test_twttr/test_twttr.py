from twttr import shorten
import pytest

def test_numeric():
    assert shorten("0")=="0"

def test_punctual():
    assert shorten(",,,")==",,,"

def test_aword():
    assert shorten("Hello")=="Hll"
    assert shorten("You")=="Y"


def test_lowercase():
    assert shorten("aeiou") == ""

def test_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("AEIOU") == ""

def test_novowels():
    assert shorten("tst n vwls") == "tst n vwls"

