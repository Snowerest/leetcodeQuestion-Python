class Node(object):
    def __init__(self, value: object, left, right) -> None:
        self.left = left
        self.right = right
        self.value = value


def generate_sort_tree(values: list) -> Node or None:
    if len(values) == 0:
        return None
    root = Node(values[0], None, None)
    for v in values[1:]:
        root = insert_into_tree(v, root)
    return root


def insert_into_tree(value: object, root: Node) -> Node:
    if root is None:
        return Node(value, None, None)
    if value <= root.value:
        root.left = insert_into_tree(value, root.left)
    else:
        root.right = insert_into_tree(value, root.right)
    return root


def pre_order(root: Node) -> Node:
    if root is None:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


if __name__ == '__main__':
    tree = generate_sort_tree([5, 6, 3, 2, 4, 1, 9, 7, 8, 0])
    print(tree)
