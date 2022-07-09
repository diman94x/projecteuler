"""Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
   Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел
   a и b - дружественным числом. Например, делителями числа 220 являются
   1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284.
   Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.
   Подсчитайте сумму всех дружественных чисел меньше 10000."""


def problem_21():
    "Функция решения задачи проекта Эейлера №21"

    def sum_divider(num):
        sum_div = 0
        for i in range(1, int(num / 2 + 1)):
            if num % i == 0:
                sum_div += i
        return sum_div

    friends_dividers = []

    for i in range(1, 10001):
        number = sum_divider(i)
        if i == sum_divider(number) and i != number:
            friends_dividers.append(i)
            friends_dividers.append(number)

    return sum(set(friends_dividers))


if __name__ == '__main__':
    print(problem_21())
