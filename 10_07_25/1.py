

def is_valid_bracket_sequence(s: str) -> bool:
    """
    Проверяет, является ли последовательность скобок в строке правильной скобочной последовательностью.

    Вход:
        s (str): строка, содержащая любые символы, в том числе скобки '(', ')', '[', ']', '{', '}'.

    Выход:
        bool: True, если последовательность скобок правильная, False — иначе.

    Примечания:
        - Все остальные символы, кроме скобок, игнорируются.
        - Правильная скобочная последовательность — это такая последовательность, в которой:
            1. Каждой открывающей скобке соответствует закрывающая скобка того же типа.
            2. Скобки правильно вложены.
    """
    
    

    d = dict(zip(')]}', '([{'))
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack.pop() != d[c]:
                return False
            
    return not stack

# Тесты для is_valid_bracket_sequence
assert is_valid_bracket_sequence("([]){}") == True
assert is_valid_bracket_sequence("([)]") == False
assert is_valid_bracket_sequence("((())") == False
assert is_valid_bracket_sequence("a(b[c]{d}e)f") == True
assert is_valid_bracket_sequence("a(b[c]{d}e") == False
assert is_valid_bracket_sequence("abc") == True
assert is_valid_bracket_sequence("") == True
assert is_valid_bracket_sequence("([{}])") == True
assert is_valid_bracket_sequence("([{}]))") == False
assert is_valid_bracket_sequence("([a+b]*{x/y}-z)") == True

print("Все тесты пройдены!")