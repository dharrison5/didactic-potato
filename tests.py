import functions

def test_add():
    assert functions.add(2, 3) == 5
    assert functions.add(-1, 1) == 0
    assert functions.add(0, 0) == 0
    assert functions.add(-5, -3) == -8

def test_subtract():
    assert functions.subtract(5, 3) == 2
    assert functions.subtract(0, 1) == -1
    assert functions.subtract(-1, -1) == 0
    assert functions.subtract(10, 20) == -10


def test_multiply():
    assert functions.multiply(2, 3) == 6
    assert functions.multiply(-1, 1) == -1
    assert functions.multiply(0, 5) == 0
    assert functions.multiply(-2, -3) == 6


if __name__ == "__main__":
    test_add()
    test_subtract()