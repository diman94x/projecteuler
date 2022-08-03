"""Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца
   в начало являются простыми числами: 197, 719 и 971.
   Существует тринадцать таких простых чисел меньше 100:
   2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
   Сколько существует круговых простых чисел меньше миллиона?"""


def problem_35():
    "Функция решения задачи проекта Эейлера №35"

    def prime_number_list(num):
        lst = [2]
        for i in range(3, num + 1, 2):
            if (i > 10) and (i % 10 == 5):
                continue
            for j in lst:
                if j * j - 1 > i:
                    lst.append(i)
                    break
                if i % j == 0:
                    break
            else:
                lst.append(i)
        return lst

    def permutation(num):
        result = []
        for i in range(len(num) - 1):
            result.append(num[-1] + num[:-1])
        return result

    prime_numbers = set(prime_number_list(1_000_000))
    result_list = []

    for number in prime_numbers:
        if number in [2, 3, 5, 7]:
            result_list.append(number)
        else:
            for num in permutation(str(number)):
                if int(num) not in prime_numbers:
                    break
            else:
                result_list.append(number)

    return len(result_list)


if __name__ == '__main__':
    print(problem_35())
