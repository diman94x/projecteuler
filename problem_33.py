"""Дробь 49/98 является любопытной, поскольку неопытный математик, пытаясь сократить ее,
   будет ошибочно полагать, что 49/98 = 4/8, являющееся истиной, получено вычеркиванием девяток.
   Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.
   Существует ровно 4 нетривиальных примера дробей подобного типа, которые меньше единицы и
   содержат двухзначные числа как в числителе, так и в знаменателе.
   Пусть произведение этих четырех дробей дано в виде несократимой дроби
   (числитель и знаменатель дроби не имеют общих сомножителей). Найдите знаменатель этой дроби."""


def problem_33():
    "Функция решения задачи проекта Эейлера №33"

    numerator = [str(i) for i in range(10, 100) if i % 10 != 0]
    denominator = [str(i) for i in range(10, 100) if i % 10 != 0]
    result_list = []
    for i in numerator:
        for j in denominator:
            if int(i) / int(j) < 1:
                if list(i)[1] == list(j)[0]:
                    if int(i[0]) / int(j[1]) == int(i) / int(j):
                        result_list.append(i + '/' + j)

    current_numerator = 1
    current_denominator = 1

    for num in result_list:
        current_numerator *= int(num[:2])
        current_denominator *= int(num[3:])

    while current_numerator != current_denominator:
        if current_numerator > current_denominator:
            current_numerator = current_numerator - current_denominator
        else:
            current_denominator = current_denominator - current_numerator

    return current_numerator


if __name__ == '__main__':
    print(problem_33())
