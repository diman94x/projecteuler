"""Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только
   вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
   Сколько существует таких маршрутов в сетке 20×20?"""


def task_15():
    "Функция решения задачи проекта Эейлера №15"

    def factorial(num):
        factorial_n = 1
        for i in range(2, num + 1):
            factorial_n *= i
        return factorial_n

    element_for_path = 40
    horizontal_element = 20

    return int(factorial(element_for_path)/
              (factorial(element_for_path - horizontal_element) * factorial(horizontal_element)))


if __name__ == '__main__':
    print(task_15())
