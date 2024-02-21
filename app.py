def square(x):
    return x ** 2


# Добавляем пустую строку после определения функции


if __name__ == "__main__":
    num = int(input("Введите число для возведения в квадрат: "))
    result = square(num)
    print(f"Квадрат числа {num} равен {result}")
