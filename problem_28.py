"""Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль
   5 на 5:

   21 22 23 24 25
   20  7  8  9 10
   19  6  1  2 11
   18  5  4  3 12
   17 16 15 14 13

   Можно убедиться, что сумма чисел в диагоналях равна 101.
   Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?"""


def problem_28():
    "Функция решения задачи проекта Эейлера №28"
    size = 1001
    sum = 1

    def current_sum(n):
        right_top = n * n
        left_top = n * n - (n - 1)
        left_bot = n * n - 2 * (n - 1)
        right_bot = n * n - 3 * (n - 1)

        return right_bot + left_bot + right_top + left_top

    for i in reversed(range(3, size + 1, 2)):
        sum += current_sum(i)

    return sum


if __name__ == '__main__':
    print(problem_28())
