"""
1. У вас есть массив чисел, составьте из них максимальное число. Например:
 [61, 228, 9] -> 961228
"""
from functools import reduce

arr = [61, 228, 9]


def max_integer(a):
    a = sorted(a, key=str, reverse=True)  # Сортировка по строкам с перестановкой
    full = int(''.join(map(str, a)))  # Объединение в 1 число
    return full


print(max_integer(arr))

# variant 2
max_int = reduce(lambda x, y: x + y, map(str, sorted(arr, key=str, reverse=True)))

print(max_int)
