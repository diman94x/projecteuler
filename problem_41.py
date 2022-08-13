"""Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до n используется в нем
   ровно один раз. К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.
   Какое существует наибольшее n-значное пан-цифровое простое число?"""


def problem_41():
    "Функция решения задачи проекта Эейлера №41"

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

    prime_numbers = set(prime_number_list(10_000_000))
    count = 0

    for num in prime_numbers:
        if int(max(str(num))) <= len(str(num)):
            counter = [0 for _ in range(0, len(str(num)) + 1)]
            for n in str(num):
                counter[int(n)] += 1
            else:
                if max(counter) == 1:
                    if len(str(num)) > count:
                        count = len(str(num))
    return count


if __name__ == '__main__':
    print(problem_41())
