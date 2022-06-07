def task_6():
    """Разность между суммой квадратов и квадратом суммы"""
    return sum([i for i in range(1, 101)]) ** 2 - sum([i*i for i in range(1, 101)])

if __name__ == '__main__':
    print(task_6())