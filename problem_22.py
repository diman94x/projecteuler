"""Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'),
   текстовый файл размером 46 КБ, содержащий более пяти тысяч имен. Начните с сортировки в
   алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте это
   значение на порядковый номер имени в отсортированном списке для получения количества очков имени.
   Например, если список отсортирован по алфавиту, имя COLIN
   (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке. Поэтому, имя
   COLIN получает 938 × 53 = 49714 очков.
   Какова сумма очков имен в файле?"""


def problem_22():
    "Функция решения задачи проекта Эейлера №22"

    with open('p022_names.txt') as file:
        names = file.readline()
    name_list = sorted([i.replace('"', '').lower() for i in names.split(',')])

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result = 0
    for name in name_list:
        current_name_result = 0
        for symbol in name:
            current_name_result += alphabet.index(symbol) + 1
        result += current_name_result * (name_list.index(name) + 1)

    return result

if __name__ == '__main__':
    print(problem_22())
