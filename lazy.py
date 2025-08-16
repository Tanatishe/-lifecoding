"""
Тест на понимание ленивых операторов and/or в Python
"""


def basic_questions():
    print("=== Базовые вопросы ===")

    # Вопрос 1.1
    print("\n1.1 Что выведет этот код?")
    print(0 and 1 and "Hello")

    # Вопрос 1.2
    print("\n1.2 Что вернет выражение?")
    print([] or "Default" or None)

    # Вопрос 1.3
    print("\n1.3 Почему all([]) возвращает True, а any([]) — False?")


def practical_examples():
    print("\n=== Практические примеры ===")

    # Вопрос 2.1
    print("\n2.1 Какой будет вывод и почему?")

    def check(x):
        print(f"Выполнена проверка для {x}")
        return x > 0

    print(check(-1) and check(2) and check(3))

    # Вопрос 2.2
    print("\n2.2 Как оптимизировать этот код?")
    print("if len(my_list) > 0 and my_list[0] == 'Admin':")


def nested_conditions():
    print("\n=== Вложенные условия ===")

    # Вопрос 3.1
    print("\n3.1 Что выведет код?")
    value = None
    print(value or (lambda: "Запасное значение")())

    # Вопрос 3.2
    print("\n3.2 Какой будет результат?")
    settings = {"color": "blue"}
    print(settings.get("color") or "red")


def danger_cases():
    print("\n=== Опасные моменты ===")

    # Вопрос 4.1
    print("\n4.1 В чем проблема этого кода?")
    user = None
    try:
        print(user.name or "Гость")
    except Exception as e:
        print(f"Ошибка: {type(e).__name__}")

    # Вопрос 4.2
    print("\n4.2 Почему это выражение может вести себя неочевидно?")
    x = 0
    y = 5
    print(x or y)


def coding_tasks():
    print("\n=== Задачи на написание кода ===")

    # Задача 5.1
    print("\n5.1 Напишите функцию safe_divide(a, b), которая возвращает a / b,")
    print("но проверяет b != 0 через ленивый and")

    # Задача 5.2
    print("\n5.2 Реализуйте обработку конфига:")
    config = {}
    print(config.get("timeout") or 30)


def run_test():
    basic_questions()
    practical_examples()
    nested_conditions()
    danger_cases()
    coding_tasks()


run_test()
