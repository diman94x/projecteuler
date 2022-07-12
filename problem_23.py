"""Совершенным числом называется число, у которого сумма его делителей равна самому числу.
   Например, сумма делителей числа 28 равна 1 + 2 + 4 + 7 + 14 = 28, что означает, что число
   28 является совершенным числом. Число n называется недостаточным, если сумма его делителей
   меньше n, и называется избыточным, если сумма его делителей больше n.
   Так как число 12 является наименьшим избыточным числом (1 + 2 + 3 + 4 + 6 = 16),
   наименьшее число, которое может быть записано как сумма двух избыточных чисел, равно 24.
   Используя математический анализ, можно показать, что все целые числа больше 28123 могут быть
   записаны как сумма двух избыточных чисел. Эта граница не может быть уменьшена дальнейшим
   анализом, даже несмотря на то, что наибольшее число, которое не может быть записано как сумма
   двух избыточных чисел, меньше этой границы.
   Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел."""

LIMIT_RANGE = 28123


def problem_23():
    "Функция решения задачи проекта Эейлера №23"

    def is_excess_number(number):
        divisors = []
        for n in range(1, int(number ** 0.5) + 1):
            if number % n == 0:
                divisors.append(n)
                if number // n not in divisors and number // n != number:
                    divisors.append(number // n)
        if sum(divisors) > number:
            return True
        return False

    excess_numbers = []
    result_numbers = []

    for i in range(1, LIMIT_RANGE + 1):
        if is_excess_number(i):
            excess_numbers.append(i)

        if excess_numbers:
            for number in excess_numbers:
                if is_excess_number(i - number):
                    break
            else:
                result_numbers.append(i)
        else:
            result_numbers.append(i)

    return sum(result_numbers)


if __name__ == '__main__':
    print(problem_23())
