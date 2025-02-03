import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

def insert_heap(root, key):
    """ Додає елемент у бінарну купу за правилами мін-купі """
    if root is None:
        return Node(key)
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node.left:
            node.left = Node(key)
            break
        else:
            queue.append(node.left)
        if not node.right:
            node.right = Node(key)
            break
        else:
            queue.append(node.right)
    return root

def build_heap(arr):
    """ Будує бінарну купу з масиву """
    if not arr:
        return None
    arr = sorted(arr)  # Сортуємо масив для формування мін-купі
    root = Node(arr[0])
    for key in arr[1:]:
        insert_heap(root, key)
    return root

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """ Додає вузли та ребра для побудови графа """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додаємо вузол
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    """ Візуалізує бінарну купу у вигляді дерева """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Тестування побудови бінарної купи
heap_elements = [10, 4, 15, 2, 8, 20, 1, 5, 30]
heap_root = build_heap(heap_elements)

# Відображення бінарної купи
draw_tree(heap_root)