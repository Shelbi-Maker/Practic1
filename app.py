def square(x):
    return x ** 2

if __name__ == "__main__":
    num = int(input("Введите число для возведения в квадрат: "))
    result = square(num)
    print(f"Квадрат числа {num} равен {result}")
