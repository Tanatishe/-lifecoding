from typing import List, Optional, Callable
from collections import deque


class TreeNode:
    """Узел бинарного дерева"""

    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


def create_sample_tree() -> TreeNode:
    """
    Создает пример бинарного дерева:
    
          1
         / \
        2   3
       / \
      4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def create_bst_tree() -> TreeNode:
    """
    Создает бинарное дерево поиска:
    
          8
         / \
        3   10
       / \    \
      1   6    14
         / \   /
        4   7 13
    """
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    return root


def print_tree(
    root: Optional[TreeNode], level: int = 0, prefix: str = "Root: "
) -> None:
    """Визуализация дерева в консоли"""
    if root is None:
        return

    print("  " * level + prefix + str(root.val))

    if root.left:
        print_tree(root.left, level + 1, "L--- ")
    if root.right:
        print_tree(root.right, level + 1, "R--- ")


# ==================== РЕКУРСИВНЫЕ ПОДХОДЫ ====================


def dfs_recursive_preorder(
    root: Optional[TreeNode], result: List[int] = None
) -> List[int]:
    """
    Рекурсивный обход в глубину: Pre-order (Корень -> Левое поддерево -> Правое поддерево)

    Args:
        root: Корень дерева
        result: Список для хранения результата (используется для рекурсии)

    Returns:
        Список значений узлов в порядке pre-order
    """
    if result is None:
        result = []

    if root is None:
        return result

    # 1. Обрабатываем корень
    result.append(root.val)

    # 2. Рекурсивно обходим левое поддерево
    dfs_recursive_preorder(root.left, result)

    # 3. Рекурсивно обходим правое поддерево
    dfs_recursive_preorder(root.right, result)

    return result


def dfs_recursive_inorder(
    root: Optional[TreeNode], result: List[int] = None
) -> List[int]:
    """
    Рекурсивный обход в глубину: In-order (Левое поддерево -> Корень -> Правое поддерево)

    Args:
        root: Корень дерева
        result: Список для хранения результата (используется для рекурсии)

    Returns:
        Список значений узлов в порядке in-order
    """
    if result is None:
        result = []

    if root is None:
        return result

    # 1. Рекурсивно обходим левое поддерево
    dfs_recursive_inorder(root.left, result)

    # 2. Обрабатываем корень
    result.append(root.val)

    # 3. Рекурсивно обходим правое поддерево
    dfs_recursive_inorder(root.right, result)

    return result


def dfs_recursive_postorder(
    root: Optional[TreeNode], result: List[int] = None
) -> List[int]:
    """
    Рекурсивный обход в глубину: Post-order (Левое поддерево -> Правое поддерево -> Корень)

    Args:
        root: Корень дерева
        result: Список для хранения результата (используется для рекурсии)

    Returns:
        Список значений узлов в порядке post-order
    """
    if result is None:
        result = []

    if root is None:
        return result

    # 1. Рекурсивно обходим левое поддерево
    dfs_recursive_postorder(root.left, result)

    # 2. Рекурсивно обходим правое поддерево
    dfs_recursive_postorder(root.right, result)

    # 3. Обрабатываем корень
    result.append(root.val)

    return result


# ==================== ИТЕРАТИВНЫЕ ПОДХОДЫ ====================


def dfs_iterative_preorder(root: Optional[TreeNode]) -> List[int]:
    """
    Итеративный обход в глубину: Pre-order с использованием стека

    Args:
        root: Корень дерева

    Returns:
        Список значений узлов в порядке pre-order
    """
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        # Извлекаем узел из стека
        node = stack.pop()

        # Обрабатываем текущий узел
        result.append(node.val)

        # Добавляем правого ребенка в стек (будет обработан после левого)
        if node.right:
            stack.append(node.right)

        # Добавляем левого ребенка в стек (будет обработан первым)
        if node.left:
            stack.append(node.left)

    return result


def dfs_iterative_inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Итеративный обход в глубину: In-order с использованием стека

    Args:
        root: Корень дерева

    Returns:
        Список значений узлов в порядке in-order
    """
    if root is None:
        return []

    result = []
    stack = []
    current = root

    while current or stack:
        # Идем влево до конца, добавляя все узлы в стек
        while current:
            stack.append(current)
            current = current.left

        # Извлекаем узел из стека и обрабатываем его
        current = stack.pop()
        result.append(current.val)

        # Переходим к правому поддереву
        current = current.right

    return result


def dfs_iterative_postorder(root: Optional[TreeNode]) -> List[int]:
    """
    Итеративный обход в глубину: Post-order с использованием двух стеков

    Args:
        root: Корень дерева

    Returns:
        Список значений узлов в порядке post-order
    """
    if root is None:
        return []

    # Используем два стека для имитации post-order обхода
    stack1 = [root]
    stack2 = []

    while stack1:
        # Извлекаем узел из первого стека
        node = stack1.pop()

        # Добавляем в второй стек
        stack2.append(node)

        # Добавляем детей в первый стек (левый будет обработан после правого)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # Извлекаем из второго стека в обратном порядке
    result = []
    while stack2:
        result.append(stack2.pop().val)

    return result


def dfs_iterative_postorder_single_stack(root: Optional[TreeNode]) -> List[int]:
    """
    Итеративный обход в глубину: Post-order с использованием одного стека

    Args:
        root: Корень дерева

    Returns:
        Список значений узлов в порядке post-order
    """
    if root is None:
        return []

    result = []
    stack = []
    current = root
    last_visited = None

    while current or stack:
        # Идем влево до конца
        while current:
            stack.append(current)
            current = current.left

        # Смотрим на верхний элемент стека
        peek = stack[-1]

        # Если у правого ребенка нет детей или мы его уже посетили
        if peek.right is None or peek.right == last_visited:
            # Обрабатываем текущий узел
            result.append(peek.val)
            last_visited = stack.pop()
        else:
            # Идем в правое поддерево
            current = peek.right

    return result


# ==================== ДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ ====================


def compare_traversals(root: TreeNode) -> None:
    """Сравнивает результаты различных типов обхода"""
    print("=" * 60)
    print("СРАВНЕНИЕ РАЗЛИЧНЫХ ТИПОВ ОБХОДА")
    print("=" * 60)

    # Рекурсивные подходы
    print("РЕКУРСИВНЫЕ ПОДХОДЫ:")
    print(f"Pre-order:  {dfs_recursive_preorder(root)}")
    print(f"In-order:   {dfs_recursive_inorder(root)}")
    print(f"Post-order: {dfs_recursive_postorder(root)}")
    print()

    # Итеративные подходы
    print("ИТЕРАТИВНЫЕ ПОДХОДЫ:")
    print(f"Pre-order:  {dfs_iterative_preorder(root)}")
    print(f"In-order:   {dfs_iterative_inorder(root)}")
    print(f"Post-order: {dfs_iterative_postorder(root)}")
    print(f"Post-order (1 стек): {dfs_iterative_postorder_single_stack(root)}")
    print()


def find_node_by_value(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """
    Поиск узла по значению с использованием DFS (pre-order)

    Args:
        root: Корень дерева
        target: Искомое значение

    Returns:
        Узел с искомым значением или None
    """
    if root is None:
        return None

    # Проверяем текущий узел
    if root.val == target:
        return root

    # Ищем в левом поддереве
    left_result = find_node_by_value(root.left, target)
    if left_result:
        return left_result

    # Ищем в правом поддереве
    return find_node_by_value(root.right, target)


def count_nodes(root: Optional[TreeNode]) -> int:
    """
    Подсчет количества узлов в дереве с использованием DFS

    Args:
        root: Корень дерева

    Returns:
        Количество узлов в дереве
    """
    if root is None:
        return 0

    # Рекурсивно считаем узлы в левом и правом поддеревьях
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def get_tree_height(root: Optional[TreeNode]) -> int:
    """
    Вычисление высоты дерева с использованием DFS

    Args:
        root: Корень дерева

    Returns:
        Высота дерева (максимальная глубина)
    """
    if root is None:
        return -1  # Пустое дерево имеет высоту -1

    # Рекурсивно вычисляем высоту левого и правого поддеревьев
    left_height = get_tree_height(root.left)
    right_height = get_tree_height(root.right)

    # Возвращаем максимальную высоту + 1 (текущий уровень)
    return max(left_height, right_height) + 1


# ==================== ТЕСТИРОВАНИЕ ====================


def run_tests() -> None:
    """Запуск всех тестов"""
    print("ТЕСТИРОВАНИЕ ОБХОДА ДЕРЕВА В ГЛУБИНУ")
    print("=" * 60)

    # Тест 1: Простое дерево
    print("ТЕСТ 1: Простое дерево")
    tree1 = create_sample_tree()
    print("Структура дерева:")
    print_tree(tree1)
    compare_traversals(tree1)

    # Тест 2: Бинарное дерево поиска
    print("ТЕСТ 2: Бинарное дерево поиска")
    tree2 = create_bst_tree()
    print("Структура дерева:")
    print_tree(tree2)
    compare_traversals(tree2)

    # Тест 3: Пустое дерево
    print("ТЕСТ 3: Пустое дерево")
    empty_tree = None
    print("Pre-order:", dfs_recursive_preorder(empty_tree))
    print("In-order:", dfs_recursive_inorder(empty_tree))
    print("Post-order:", dfs_recursive_postorder(empty_tree))
    print()

    # Тест 4: Дерево с одним узлом
    print("ТЕСТ 4: Дерево с одним узлом")
    single_node = TreeNode(42)
    print("Pre-order:", dfs_recursive_preorder(single_node))
    print("In-order:", dfs_recursive_inorder(single_node))
    print("Post-order:", dfs_recursive_postorder(single_node))
    print()

    # Тест 5: Дополнительные функции
    print("ТЕСТ 5: Дополнительные функции")
    print(f"Количество узлов в дереве: {count_nodes(tree1)}")
    print(f"Высота дерева: {get_tree_height(tree1)}")

    # Поиск узла
    target_value = 5
    found_node = find_node_by_value(tree1, target_value)
    if found_node:
        print(f"Узел со значением {target_value} найден: {found_node.val}")
    else:
        print(f"Узел со значением {target_value} не найден")

    # Поиск несуществующего узла
    target_value = 99
    found_node = find_node_by_value(tree1, target_value)
    if found_node:
        print(f"Узел со значением {target_value} найден: {found_node.val}")
    else:
        print(f"Узел со значением {target_value} не найден")
    print()


if __name__ == "__main__":
    run_tests()
