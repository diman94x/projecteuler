"""Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со знаменателями
   от 2 до 10 даны ниже:

   1/2	=  0.5
   1/3	=  0.(3)
   1/4	=  0.25
   1/5	=  0.2
   1/6	=  0.1(6)
   1/7	=  0.(142857)
   1/8	=  0.125
   1/9	=  0.(1)
   1/10	=  0.1
   Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры.
   Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.
   Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную
   повторяющуюся последовательность цифр."""


def problem_26():
    "Функция решения задачи проекта Эейлера №26"

    denominators = range(2, 1001)
    results = []

    for d in denominators:
        current_num = []
        numerator = 1
        while not current_num.count(numerator):
            current_num.append(numerator)
            numerator = 10 * numerator % d
        results.append(len(current_num) - current_num.index(numerator))

    return max(results)


if __name__ == '__main__':
    print(problem_26())
