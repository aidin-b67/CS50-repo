from fuel import convert, gauge
import pytest
def main():

    test_ZeroDivisionError()
    test_correct_input()
    test_ValueError()

def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")



def test_correct_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

if __name__ == "__main__":
    main()