# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def negafibonacci(number: int):
    a, b = 1, 1
    numbers_list = [0]


    for i in range(number):
        numbers_list.append(a)
        numbers_list.insert(0, a * (-1) ** i)
        a, b = b, b + a

    return numbers_list


print(*negafibonacci(int(input('Задайте число: '))))
