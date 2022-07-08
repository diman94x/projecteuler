"""n! означает n × (n − 1) × ... × 3 × 2 × 1
Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Найдите сумму цифр в числе 100!."""


def problem_20():
    "Функция решения задачи проекта Эейлера №20"

    def factorial(num):
        if num == 0:
            return 1
        return factorial(num - 1) * num

    return sum((int(i) for i in list(str(factorial(100)))))


if __name__ == '__main__':
    print(problem_20())
