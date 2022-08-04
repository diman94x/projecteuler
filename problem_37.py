"""Число 3797 обладает интересным свойством. Будучи само по себе простым числом, из него можно
   последовательно выбрасывать цифры слева направо, число же при этом остается простым на каждом
   этапе: 3797, 797, 97, 7. Точно таким же способом можно выбрасывать цифры справа налево:
   3797, 379, 37, 3.
   Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как
   справа налево, так и слева направо, но числа при этом остаются простыми.
   ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются."""


def problem_37():
    "Функция решения задачи проекта Эейлера №37"

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

    prime_numbers = set(prime_number_list(1_000_000))
    result = []

    for num in prime_numbers:
        if num not in [2, 3, 5, 7]:
            number = str(num)
            for i, _ in enumerate(number):
                if int(number[:i+1]) not in prime_numbers or int(number[::-1][i::-1]) not in prime_numbers:
                    break
            else:
                result.append(num)

    return sum(result)


if __name__ == '__main__':
    print(problem_37())
