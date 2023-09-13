# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

import itertools

def simple_num(n):
    list1 = []
    count = 0
    for i in itertools.count(2):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            list1.append(i)
            count = 0
            yield i
            if len(list1) == n:
                break
        else:
            count = 0

print(*simple_num(50))

