"""145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
   Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.
   Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует."""


def problem_34():
    "Функция решения задачи проекта Эейлера №34"

    cache = {1: 1, 2: 2}

    def factorial(number):
        if number in cache:
            return cache[number]
        elif number == 0:
            return 1
        else:
            x = factorial(number - 1) * number
            cache[number] = x
            return x

    result = []

    for i in range(3, 10000000):
        current_number = 0
        for n in str(i):
            current_number += factorial(int(n))
        if i == current_number:
            result.append(i)
            print(i)

    return result


if __name__ == '__main__':
    print(problem_34())
