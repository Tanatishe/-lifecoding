




def find_max_subarray(nums: list[int], max_length: int = 2) -> tuple[list[int], int]:
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]
    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    check_dict = {nums[0]: 0, nums[1]: 1}
    max_sum = prefix_sum[1]
    best_left = 0
    best_right = 1
    left = 0
    right = 1
    while right < len(nums):
        check_dict[nums[right]] = right
        if len(check_dict) > max_length:
            min_index = min(check_dict.values())
            check_dict.pop(nums[min_index])
            left = min_index + 1

        temp_sum = (
            prefix_sum[right] if left == 0 else prefix_sum[right] - prefix_sum[left - 1]
        )
        if temp_sum > max_sum:
            max_sum = temp_sum
            best_left = left
            best_right = right
        right += 1
    return nums[best_left : best_right + 1], max_sum


# Тест 1: обычный случай
arr = [3, 5, 6, 10, 5, 10, 5, 8]
expected = ([10, 5, 10, 5], 30)
result = find_max_subarray(arr)
print(f"Test 1: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 2: все элементы одинаковые
arr = [7, 7, 7, 7, 7]
expected = ([7, 7, 7, 7, 7], 35)
result = find_max_subarray(arr)
print(f"Test 2: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 3: все элементы разные
arr = [1, 2, 3, 4, 5]
expected = ([4, 5], 9)
result = find_max_subarray(arr)
print(f"Test 3: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 4: массив из двух чисел
arr = [9, 4]
expected = ([9, 4], 13)
result = find_max_subarray(arr)
print(f"Test 4: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 5: максимальный подмассив в начале
arr = [8, 8, 9, 10, 11]
expected = ([8, 8, 9], 25)
result = find_max_subarray(arr)
print(f"Test 5: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 6: короткий массив из одинаковых чисел
arr = [2, 2]
expected = ([2, 2], 4)
result = find_max_subarray(arr)
print(f"Test 6: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 7: длинный массив с чередованием
arr = [1, 2, 1, 2, 1, 2, 1, 2]
expected = ([1, 2, 1, 2, 1, 2, 1, 2], 12)
result = find_max_subarray(arr)
print(f"Test 7: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 8: массив с большими числами
arr = [1000, 2000, 1000, 2000, 1000]
expected = ([1000, 2000, 1000, 2000, 1000], 7000)
result = find_max_subarray(arr)
print(f"Test 8: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 9: максимальный подмассив в конце
arr = [3, 4, 5, 6, 7, 7, 8, 8, 8]
expected = ([7, 7, 8, 8, 8], 38)
result = find_max_subarray(arr)
print(f"Test 9: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 10: максимальный подмассив в начале
arr = [9, 9, 10, 11, 12]
expected = ([9, 9, 10], 28)
result = find_max_subarray(arr)
print(f"Test 10: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 11: один повторяющийся и один отличный
arr = [5, 5, 5, 1, 5, 5]
expected = ([5, 5, 5, 1, 5, 5], 26)
result = find_max_subarray(arr)
print(f"Test 11: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 12: все числа разные
arr = [1, 2, 3, 4, 5, 6]
expected = ([5, 6], 11)
result = find_max_subarray(arr)
print(f"Test 12: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 13: два больших блока разных чисел
arr = [2] * 5 + [3] * 4
expected = ([2, 2, 2, 2, 2, 3, 3, 3, 3], 22)
result = find_max_subarray(arr)
print(f"Test 13: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 14: максимальный подмассив — весь массив
arr = [4, 4, 5, 5, 4, 5]
expected = ([4, 4, 5, 5, 4, 5], 27)
result = find_max_subarray(arr)
print(f"Test 14: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

# Тест 15: несколько одинаковых максимальных подмассивов
arr = [1, 2, 1, 2, 1, 2]
expected = ([1, 2, 1, 2, 1, 2], 9)
result = find_max_subarray(arr)
print(f"Test 15: {arr}\n  Ожидается: {expected}\n  Получено: {result}\n")
assert result == expected

print("it's ok")
