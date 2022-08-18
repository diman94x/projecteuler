"""Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:
   Треугольные	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
   Пятиугольные	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
   Шестиугольные	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
   Можно убедиться в том, что T285 = P165 = H143 = 40755.
   Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным."""


def problem_45():
    "Функция решения задачи проекта Эейлера №45"

    max_range = 60000
    previous = 40755

    first_num = set(int(n * (n + 1) / 2) for n in range(2, max_range))
    second_num = set(int(n * (3 * n - 1) / 2) for n in range(2, max_range)
                     if int(n * (3 * n - 1) / 2) in first_num)
    third_num = list(int(n * (2 * n - 1)) for n in range(2, max_range)
                     if int(n * (2 * n - 1)) in second_num)

    return third_num[third_num.index(previous) + 1] if len(third_num) >= 2 else False


if __name__ == '__main__':
    print(problem_45())
