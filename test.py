# Импортируем функцию, которую мы хотим протестировать
import unittest
from app import square


# Тесты для функции square
def test_square_positive():
    # Проверяем, что квадрат положительного числа вычисляется правильно
    assert square(2) == 4


def test_square_negative():
    # Проверяем, что квадрат отрицательного числа вычисляется правильно
    assert square(-3) == 9


def test_square_zero():
    # Проверяем, что квадрат нуля равен нулю
    assert square(0) == 0


def test_square_fraction():
    # Проверяем, что квадрат дробного числа вычисляется правильно
    assert square(2.5) == 6.25
