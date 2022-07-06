"""Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
   Найдите сумму всех простых чисел меньше двух миллионов."""


def problem_10():
    "Функция решения задачи проекта Эейлера №10"

    def is_prime_number(num):
        if num in (2, 3):
            return True
        if num % 2 == 0 or num < 2:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    simply_numbers = (i for i in range(2, 2_000_001) if is_prime_number(i))
    return sum(simply_numbers)

if __name__ == '__main__':
    print(problem_10())
