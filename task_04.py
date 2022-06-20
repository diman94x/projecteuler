def task_4():
    """Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
       Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
       Найдите самый большой палиндром, полученный умножением двух трехзначных чисел."""

    range_numbers_first = reversed(range(100, 1000))
    palindrome_numbers = []
    for number in range_numbers_first:
        range_numbers_second = reversed(range(100, number + 1))
        for num in range_numbers_second:
            if str(num * number) == str(num * number)[::-1]:
                palindrome_numbers.append(num * number)
    return max(palindrome_numbers)


if __name__ == '__main__':
    print(task_4())