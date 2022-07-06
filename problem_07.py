"""Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число
   - 13. Какое число является 10001-м простым числом?"""

def problem_7():
    "Функция решения задачи проекта Эейлера №7"

    simple_numbers = [2, 3, 5, 7, 11, 13]
    next_test_numbers = simple_numbers[-1]
    while len(simple_numbers) < 10001:
        next_test_numbers += 2
        for number in simple_numbers:
            if next_test_numbers % number == 0:
                break
        else:
            simple_numbers.append(next_test_numbers)
    return simple_numbers


if __name__ == '__main__':
    print(problem_7())