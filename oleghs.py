import random


# выбор- кто начинает из num количества игроков
def who_is_started(num=2):
    return random.randint(1, num)


# num = 5
print(who_is_started())
# print(random.randint(1,2))

# initialization hands for example
a = [[3, 5], [2, 3], [1, 6], [3, 3], [2, 7], [4, 2], [1, 5]]
b = [[2, 4], [3, 5], [2, 3], [1, 2], [3, 5], [2, 4], [2, 6]]

# вывод пятого элемента второго разряда ( от нуля счет)
print(a[4][1])  # 7

# уменьшение хп пятого элемента на количество его урона
a[4][1] = a[4][1] - a[4][0]

# проверка его текущей жизни
print(a[4][1])  # 5 - работает принцип !)

# а начинает, первая карта
# определяем урон
print(f"урон {a[0][0]}")

# выбираем случайного противника
enemy_card_num = random.randint(0, len(b)-1)
print(enemy_card_num)
b[enemy_card_num][1] -= a[0][0]

# смотрим на текущее здоровье
print(b)
