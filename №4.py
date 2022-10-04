# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

from random import uniform


def rand_nums(count: int):
    numbers = []
    if count <= 0:
        print("Отрицательное значение")
        return [0.0]

    for i in range(count):
        numbers.append(round(uniform(1, count), 2))
    return numbers


def max_min(numbers: list):
    maximum = minimum = numbers[0] % 1

    for k in range(1, len(numbers)):
        number = round(numbers[k] % 1, 2)
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number

    res = round(maximum - minimum, 2)
    print(f"Минимальное: {minimum}, Максимальное: {maximum}. Разница: {res}")
    return res


final_list = rand_nums(int(input("Задайте кол-во вещественных чисел: ")))
print(final_list)
print(max_min(final_list))