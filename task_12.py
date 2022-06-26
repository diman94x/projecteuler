"""Последовательность треугольных чисел образуется путем сложения натуральных чисел.
К примеру, 7-е треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
Первые десять треугольных чисел:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.
Каково первое треугольное число, у которого более пятисот делителей?"""


def task_12():
    "Функция решения задачи проекта Эейлера №12"
    numbers_range = (int(0.5 * n * (n + 1)) for n in range(20000))

    def is_prime_number(num):
        if num in (2, 3):
            return True
        if num % 2 == 0 or num < 2:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    for number in numbers_range:
        prime_numbers = []
        for i in range(2, int(number ** 0.5)):
            if is_prime_number(i):
                prime_numbers.append(i)
        if prime_numbers:
            count_n_prime = [0] * len(prime_numbers)
            current_number = number
            index = 0
            while index < len(prime_numbers):
                if current_number % prime_numbers[index] != 0:
                    index += 1
                else:
                    current_number = current_number / prime_numbers[index]
                    count_n_prime[index] += 1
            dividers = 1
            for n in count_n_prime:
                dividers = dividers * (n + 1)
            if dividers > 500:
                return number


if __name__ == '__main__':
    print(task_12())
