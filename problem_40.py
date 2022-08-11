"""Дана иррациональная десятичная дробь, образованная объединением натуральных чисел:
   0.123456789101112131415161718192021...
   Видно, что 12-я цифра дробной части - 1.
   Также дано, что dn представляет собой n-ю цифру дробной части.
   Найдите значение следующего выражения:
   d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""


def problem_40():
    "Функция решения задачи проекта Эейлера №40"
    numbers_list = []
    for i in range(1, 1_000_000):
        numbers_list.append(str(i))

    number = '0' + ''.join(numbers_list)

    num = [int(number[int('1' + (i * '0'))]) for i in range(0, 7)]

    def multiply(lst):
        answer = 1
        for i in lst:
            answer *= i
        return answer

    return multiply(num)


if __name__ == '__main__':
    print(problem_40())
