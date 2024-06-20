from um import count
import pytest
import re

def test_normal_case():
    assert count("um")==1
    assert count("um?")==1
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2

# def test_biggermin():
#     with pytest.raises(ValueError):
#         count("cat")

# def test_character():
#     with pytest.raises(ValueError):
#         count("???")

def test_multiple():
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2

def test_cases():
    assert count("UM, THANKS FOR THE ALBUM")==1
    assert count("UM, THANKS, UM...")==2