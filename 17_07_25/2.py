"""
дан массив чисел nums и число target. Найти подпоследовательность в nums,
сумма элементов которой равна target
Пример:
nums = [1, 3, 76, 21, 1, 2, 45, 8, 33]
target = 24
result = [21, 1, 2]
"""


def find_subsequence_with_sum_prefix(nums, target):
    # Решение за O(n) с помощью префиксных сумм и словаря
    prefix_sum = 0
    prefix_map = {0: -1}  # сумма: индекс последнего элемента с этой суммой
    for i, num in enumerate(nums):
        prefix_sum += num
        if (prefix_sum - target) in prefix_map:
            start = prefix_map[prefix_sum - target] + 1
            return nums[start : i + 1]
        prefix_map[prefix_sum] = i
    return []


# Тесты
nums1 = [1, 3, 76, 21, 1, 2, 45, 8, 33]
target1 = 24
assert find_subsequence_with_sum_prefix(nums1, target1) == [21, 1, 2]

# Нет подходящей подпоследовательности
nums2 = [1, 2, 3]
target2 = 100
assert find_subsequence_with_sum_prefix(nums2, target2) == []

# Несколько вариантов, возвращается первый
nums3 = [5, 5, 5, 5]
target3 = 10
assert find_subsequence_with_sum_prefix(nums3, target3) == [5, 5]

# Пустой массив
nums4 = []
target4 = 0
assert find_subsequence_with_sum_prefix(nums4, target4) == []

# target = 0, есть 0 в массиве
nums5 = [1, 0, 2]
target5 = 0
assert find_subsequence_with_sum_prefix(nums5, target5) == [0]

# Отрицательные числа
nums6 = [2, -1, 3, 1, -2, 4]
target6 = 2
assert find_subsequence_with_sum_prefix(nums6, target6) == [2]

nums7 = [2, -1, 3, 1, -2, 4]
target7 = 5
assert find_subsequence_with_sum_prefix(nums7, target7) == [2, -1, 3, 1]

print("Все тесты для 2.py пройдены!")
