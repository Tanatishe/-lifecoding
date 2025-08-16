"""
Напишите программу, которая принимает на вход n строк. Каждая строка содержит ключ и, возможно, значение, разделённые одним пробелом.
Ваша задача — создать в словаре пару на основании введенных данных по следующему принципу:

Если значение отсутствует, создайте в словаре ключ с значением None;
Если один и тот же ключ встречается несколько раз, последующее значение должно заменять предыдущее.
В конце программа должна вывести итоговый словарь.

Особое внимание обратите на второй тест

Sample Input 1:
4
product Apple
price 10
product Banana
availability
Sample Output 1:
{'product': 'Banana', 'price': '10', 'availability': None}

Sample Input 2:
5
name John
age 25
city New York
country
age 30
Sample Output 2:
{'name': 'John', 'age': '30', 'city': 'New York', 'country': None}
"""


def parse_input_to_dict(lines):
    d = {}
    for line in lines:
        parts = line.strip().split(" ", 1)
        if len(parts) == 2:
            key, value = parts
        else:
            key, value = parts[0], None
        d[key] = value
    return d


# Тесты
# Пример 1 из условия
lines1 = ["product Apple", "price 10", "product Banana", "availability"]
assert parse_input_to_dict(lines1) == {
    "product": "Banana",
    "price": "10",
    "availability": None,
}

# Пример 2 из условия
lines2 = ["name John", "age 25", "city New York", "country", "age 30"]
assert parse_input_to_dict(lines2) == {
    "name": "John",
    "age": "30",
    "city": "New York",
    "country": None,
}

# Ключ без значения
lines3 = ["key1", "key2 value2"]
assert parse_input_to_dict(lines3) == {"key1": None, "key2": "value2"}

# Повторяющиеся ключи
lines4 = ["a 1", "a 2", "a"]
assert parse_input_to_dict(lines4) == {"a": None}

# Пустой ввод
lines5 = []
assert parse_input_to_dict(lines5) == {}

print("Все тесты пройдены!")
