# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

def convert(num: int):
    numbers = []

    while num > 0:
        numbers.insert(0, num % 2)
        num //= 2

    print(*numbers, sep="")


convert(int(input('Введите десятичное число: ')))