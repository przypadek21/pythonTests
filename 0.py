# zadanie 0
# czy osoba o padanym wieku jest pełnoletnia
import pytest


def is_adult(age: int) -> bool:
    return age >= 18

def test_is_adult():
    # given
    age = 19
    # when (opisujemy to o sie wydarza)
    result = is_adult(age)
    # then (sprawzenie poprawnosci)
    assert result # jezeli to o jest za assert bedzie prawda to test bedzie poprawny


def test_is_not_ault():
    assert not is_adult(17)
    assert not is_adult(3)