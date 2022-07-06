"""Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a**2 + b**2 = c**2
Например, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc."""


def problem_9():
    "Функция решения задачи проекта Эейлера №9"

    num_list = ([a, b, int((a ** 2 + b ** 2) ** 0.5)] for a in range(1, 1000)
                for b in range(1, 1000) if a < b and ((a ** 2 + b ** 2) ** 0.5).is_integer())
    search_nums = []
    for num in num_list:
        if num[0] + num[1] + num[2] == 1000:
            search_nums = num
    return search_nums


if __name__ == '__main__':
    print(problem_9())
