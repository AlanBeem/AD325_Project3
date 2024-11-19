from binary_search_tree import Node

def levelorder_traversal(node: Node):
    """Breadth-first search. For BST returns a list of nodes in order of height starting with the root."""
    queue = []
    this_level = [node]
    next_level = [node.left, node.right]
    while not all([this_level[i] is None for i in range(len(this_level))]):
        queue.extend(this_level)
        this_level = next_level
        next_level = []
        for each in this_level:
            if each is not None:
                next_level.append(each.left)
                next_level.append(each.right)
    level_list = []
    for each in queue:
        if each is not None:
            level_list.append(each)
    return level_list


def left_diagonal_traversal(node: Node):
    pass


def right_diagonal_traversal(node: Node):
    pass

