from working import convert
import pytest
import re


def test_normal_case():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
    assert convert("10 PM to 8 AM")=="22:00 to 08:00"

def test_biggermin():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("10:99 PM to 8 AM")

def test_biggerhour():
    with pytest.raises(ValueError):
        convert("13 AM to 9 PM")
        convert("9 AM to 25 PM")


def test_textorothers():
    with pytest.raises(ValueError):
        convert("cat")
        convert("...")
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")