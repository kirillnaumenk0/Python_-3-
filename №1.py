# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22


from random import sample


def random_numbers(count: int):
    if count < 0:
        print("Отрицательное значение")
        return []

    numbers = sample(range(1, count * 2), count)
    return numbers


def sum_odd_pos(numbers: list):
    sum_numbers = 0
    for k in range(0, len(numbers), 2):
        sum_numbers += numbers[k]
    return sum_numbers


final_list = random_numbers(int(input("Введите число: ")))
print(final_list)
print(sum_odd_pos(final_list))