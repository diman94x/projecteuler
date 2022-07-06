"""Простые делители числа 13195 - это 5, 7, 13 и 29.
   Каков самый большой делитель числа 600851475143, являющийся простым числом?"""


def problem_3():
    "Функция решения задачи проекта Эейлера №3"

    number = 600851475143

    def is_prime_number(num):
        if num in [2, 3]:
            return True
        if num % 2 == 0 or num < 2:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    for i in range(1, number):
        if number % i == 0:
            if is_prime_number(int(number / i)):
                return int(number / i)


if __name__ == '__main__':
    print(problem_3())
