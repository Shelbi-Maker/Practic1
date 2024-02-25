from app import square

def test_sqr_5():
    assert square(5) == 30

def test_sqr_8():
    assert square(8) == 80

def test_sqr_0():
    assert square(0) == 0

def test_sqr_10():
    assert square(10) == 100

def test_sqr_1():
    assert square(1) == 1
