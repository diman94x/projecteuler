"""Задача 27
   Квадратичные простые числа"""


def problem_27():
    "Функция решения задачи проекта Эейлера №27"

    def prime_number_list(num):
        n = num
        lst = [2]
        for i in range(3, n + 1, 2):
            if (i > 10) and (i % 10 == 5):
                continue
            for j in lst:
                if j * j - 1 > i:
                    lst.append(i)
                    break
                if (i % j == 0):
                    break
            else:
                lst.append(i)
        return lst

    def formula(a_f, b_f, n_f):
        return abs((n_f * n_f) + (a_f * n_f) + b_f)

    prime_numbers = set(prime_number_list(1_000_000))

    result_dict = {}

    a = range(-999, 1000)
    b = range(-1000, 1001)

    for num_a in a:
        for num_b in b:
            current_n = 0
            while True:
                if formula(num_a, num_b, current_n) in prime_numbers:
                    current_n += 1
                else:
                    result_dict[current_n] = (num_a, num_b)
                    break

    return result_dict[max(result_dict)][0] * result_dict[max(result_dict)][1]


if __name__ == '__main__':
    print(problem_27())
