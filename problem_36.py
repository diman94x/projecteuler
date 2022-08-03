"""Десятичное число 585 = 1001001001 (в двоичной системе), является палиндромом по обоим основаниям
   Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.
   (Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из
   оснований)."""


def problem_36():
    "Функция решения задачи проекта Эейлера №36"

    def is_palindrome(number):
        if number == number[::-1] and number[::-1][0] != '0':
            if str(bin(int(number)))[2:] == str(bin(int(number)))[:1:-1] and \
                    str(bin(int(number)))[:1:-1][0] != '0':
                return True
        return False

    return sum((i for i in range(1, 1_000_001) if is_palindrome(str(i)) is True))


if __name__ == '__main__':
    print(problem_36())
