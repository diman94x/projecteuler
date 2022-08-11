"""Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c},
   то существует ровно три решения для p = 120:
   {20,48,52}, {24,45,51}, {30,40,50}
   Какое значение p ≤ 1000 дает максимальное число решений?"""


def problem_39():
    "Функция решения задачи проекта Эейлера №39"
    '''a**2 + b**2 = c**2 
       p = a + b + c'''

    cache_list = []

    for a in range(1, 1001):
        for b in range(1, 1001):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer():
                p = int(c) + a + b
                if p <= 1000:
                    cache_list.append([p, int(c), a, b])

    result_dict = {i: 0 for i in range(1, 1001)}

    for i, item in enumerate(cache_list):
        for j in cache_list[i + 1:]:
            if item[0] == j[0] and item[1] in j and item[2] in j:
                break
        else:
            result_dict.update({item[0]: result_dict[item[0]] + 1})

    return max(result_dict, key=result_dict.get)


if __name__ == '__main__':
    print(problem_39())
