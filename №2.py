# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample


def random_numbers(count):
    if count < 0:
        print("Отрицательное число")
        return []

    numbers = sample(range(1, count * 2), count)
    return numbers


def pairs_nums(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list


final_list = random_numbers(int(input("Введите число: ")))
print(final_list)
print(pairs_nums(final_list))