"""
Допустим, у вас есть список чисел, и вы хотите разбить его на возрастающие фрагменты — участки, где каждое следующее число
больше предыдущего.
Такая задача может пригодиться при анализе последовательностей, графиков или пользовательских действий.

Напишите функцию fragments(numbers), которая принимает список целых чисел и возвращает список вложенных списков — каждый
из которых представляет собой возрастающий отрезок исходной последовательности.
"""


def fragments(numbers):
    if not numbers:
        return []
    result = []
    current = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current.append(numbers[i])
        else:
            result.append(current)
            current = [numbers[i]]
    result.append(current)
    return result


# Тесты
# Обычный случай
nums1 = [1, 2, 2, 3, 4, 1, 2]
assert fragments(nums1) == [[1, 2], [2, 3, 4], [1, 2]]

# Все возрастают
nums2 = [1, 2, 3, 4]
assert fragments(nums2) == [[1, 2, 3, 4]]

# Все убывают
nums3 = [4, 3, 2, 1]
assert fragments(nums3) == [[4], [3], [2], [1]]

# Один элемент
nums4 = [42]
assert fragments(nums4) == [[42]]

# Пустой список
nums5 = []
assert fragments(nums5) == []

# Случай с чередованием
nums6 = [1, 3, 2, 4, 3, 5]
assert fragments(nums6) == [[1, 3], [2, 4], [3, 5]]

print("Все тесты для 3.py пройдены!")
