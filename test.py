from app import square


def test_square_positive():
    assert square(2) == 4  # Проверка квадрата положительного числа


def test_square_negative():
    assert square(-3) == 9  # Проверка квадрата отрицательного числа
