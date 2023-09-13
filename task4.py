# Создайте функцию генератор чисел Фибоначчи

import itertools

# def fibon(n):
#     first = 0
#     second = 1
#     count = 0
#     while count < n:
#         first,second = second, first+second
#         yield second
#         count += 1

# print(*fibon(10))

def fibon():
    first = 0
    second = 1
    for _ in itertools.count():
        yield second
        first,second = second, first+second

iterat = fibon()
print(next(iterat))
print(next(iterat))
print(next(iterat))
print(next(iterat))
print(next(iterat))
