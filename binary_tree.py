class Node(object):
     def __init__(self, value: object, left: Node, right: Node) -> None:
         self.left = left
         self.right = right
         self.value = value
         
def generate_sort_tree(values: list) -> Node:
    node = Node()
         
