def task_5():
    """2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
       Какое самое маленькое число делится нацело на все числа от 1 до 20?"""

    current_number = 0
    while True:
        current_number += 1
        print('Current number', current_number)
        n = 20
        while n >= 1:
            if current_number % n == 0:
                n -= 1
            else:
                break
        else:
            return current_number


if __name__ == '__main__':
    print(task_5())