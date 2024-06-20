from datetime import date
import sys
import inflect
import re
from seasons import check
import pytest

def test_normal_case():
    assert check("2022-02-14")==date(2022,2,14)
    assert check("2021-02-14")==date(2021,2,14)


def test_wrongformat():
    with pytest.raises(SystemExit):
        check("2022.02.14")
        check("Jan 20,1996")