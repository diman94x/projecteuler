"""Следующая повторяющаяся последовательность определена для множества натуральных чисел:
n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)
Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается,
что все сгенерированные таким образом последовательности оканчиваются на 1.
Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?
Примечание: Следующие за первым элементы последовательности могут быть больше миллиона."""


def problem_14():
    "Функция решения задачи проекта Эейлера №14"

    cache = {}
    for i in range(1, 1_000_000):
        count = 1
        current_start_num = i
        while current_start_num > 1:
            if cache.get(current_start_num):
                cache.update({i: cache.get(current_start_num) + count})
                break
            if current_start_num % 2 == 0:
                current_start_num = current_start_num / 2
            else:
                current_start_num = current_start_num * 3 + 1
            count += 1
        else:
            cache.update({i: count})

    return list(cache.values()).index(max(cache.values())) + 1


if __name__ == '__main__':
    print(problem_14())
