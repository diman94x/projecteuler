def task_2():
    """Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
       1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
       Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона."""

    fibonacci_list = [1, 2]

    def next_element(prev_previous_element, previous_element):
        return prev_previous_element + previous_element

    while next_element(fibonacci_list[-2], fibonacci_list[-1]) <= 4000000:
        fibonacci_list.append(next_element(fibonacci_list[-2], fibonacci_list[-1]))
    return sum([i for i in fibonacci_list if i % 2 == 0])


if __name__ == '__main__':
    print(task_2())
