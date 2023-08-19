from bank import value

def main():
    test_return_zero()
    test_return_20()
    test_return_100()


def test_return_zero():
    assert value("HELLO") == 0
    assert value("HeLlo Gi") == 0
    assert value("hello gi") == 0

def test_return_20():
    assert value("hi") == 20
    assert value("hey") == 20

def test_return_100():
    assert value("What") == 100
    assert value("Good_morning") == 100


