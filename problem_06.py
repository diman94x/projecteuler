"""Разность между суммой квадратов и квадратом суммы"""

def problem_6():
    "Функция решения задачи проекта Эейлера №6"

    return sum((i for i in range(1, 101))) ** 2 - sum((i * i for i in range(1, 101)))


if __name__ == '__main__':
    print(problem_6())
