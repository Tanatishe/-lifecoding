class TreeNode:
    """Узел бинарного дерева"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_traversal_analysis():
    """
    ЗАДАЧА: Анализ обхода бинарного дерева
    
    У вас есть бинарное дерево:
    
           10
          /  \\
         5    15
        / \\   / \\
       3   7 12  18
      /     \\
     1       9
    
    ВАША ЗАДАЧА:
    1. Реализовать обход в глубину (DFS) - inorder, preorder, postorder
    2. Реализовать обход в ширину (BFS) - level order
    3. Найти максимальную глубину дерева
    4. Найти сумму всех узлов дерева
    5. Найти количество листьев (узлов без потомков)
    6. Найти путь от корня до узла с заданным значением
    7. Проверить, является ли дерево сбалансированным
    8. Найти самый широкий уровень (уровень с максимальным количеством узлов)
    
    ТРЕБУЕТСЯ:
    - Рекурсивные алгоритмы обхода
    - Использование стеков и очередей
    - Работа с деревьями и узлами
    - Поиск в глубину и ширину
    - Анализ структуры дерева
    
    ВЕРНУТЬ: кортеж (inorder, preorder, postorder, level_order, max_depth, sum_nodes, leaf_count, path_to_node, is_balanced, widest_level)
    """

    # Создаем дерево из примера
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)
    root.left.left.left = TreeNode(1)
    root.left.right.right = TreeNode(9)


# ТЕСТЫ
if __name__ == "__main__":
    result = tree_traversal_analysis()
    (
        inorder,
        preorder,
        postorder,
        level_order,
        depth,
        total_sum,
        leaves,
        path_to_7,
        balanced,
        widest,
    ) = result

    # Тест 1: Проверка inorder обхода
    expected_inorder = [1, 3, 5, 7, 9, 10, 12, 15, 18]
    assert (
        inorder == expected_inorder
    ), f"Inorder должен быть {expected_inorder}, получено: {inorder}"

    # Тест 2: Проверка preorder обхода
    expected_preorder = [10, 5, 3, 1, 7, 9, 15, 12, 18]
    assert (
        preorder == expected_preorder
    ), f"Preorder должен быть {expected_preorder}, получено: {preorder}"

    # Тест 3: Проверка postorder обхода
    expected_postorder = [1, 3, 9, 7, 5, 12, 18, 15, 10]
    assert (
        postorder == expected_postorder
    ), f"Postorder должен быть {expected_postorder}, получено: {postorder}"

    # Тест 4: Проверка level order обхода
    expected_level_order = [[10], [5, 15], [3, 7, 12, 18], [1, 9]]
    assert (
        level_order == expected_level_order
    ), f"Level order должен быть {expected_level_order}, получено: {level_order}"

    # Тест 5: Проверка максимальной глубины
    assert depth == 4, f"Максимальная глубина должна быть 4, получено: {depth}"

    # Тест 6: Проверка суммы всех узлов
    assert total_sum == 80, f"Сумма всех узлов должна быть 80, получено: {total_sum}"

    # Тест 7: Проверка количества листьев
    assert leaves == 4, f"Количество листьев должно быть 4, получено: {leaves}"

    # Тест 8: Проверка пути к узлу 7
    expected_path = [10, 5, 7]
    assert (
        path_to_7 == expected_path
    ), f"Путь к узлу 7 должен быть {expected_path}, получено: {path_to_7}"

    # Тест 9: Проверка сбалансированности
    assert (
        balanced == True
    ), f"Дерево должно быть сбалансированным, получено: {balanced}"

    # Тест 10: Проверка самого широкого уровня
    assert (
        widest == 4
    ), f"Самый широкий уровень должен содержать 4 узла, получено: {widest}"

    print("Все тесты прошли успешно!")
    print(f"Inorder: {inorder}")
    print(f"Preorder: {preorder}")
    print(f"Postorder: {postorder}")
    print(f"Level order: {level_order}")
    print(f"Максимальная глубина: {depth}")
    print(f"Сумма всех узлов: {total_sum}")
    print(f"Количество листьев: {leaves}")
    print(f"Путь к узлу 7: {path_to_7}")
    print(f"Сбалансированное: {balanced}")
    print(f"Самый широкий уровень: {widest} узлов")
