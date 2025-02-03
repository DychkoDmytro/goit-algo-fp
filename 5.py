import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додає вузли та ребра для побудови графа"""
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def generate_colors(n):
    """Генерує градацію кольорів від темного до світлого"""
    return ["#{:02X}{:02X}{:02X}".format(int(c * 255), int(c * 180), int(c * 240)) for c in [i / (n + 1) for i in range(1, n + 1)]]

def draw_tree(tree_root, visited_nodes, title):
    """Візуалізує дерево з підсвіченими вузлами згідно порядку обходу"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    colors = generate_colors(len(visited_nodes))

    node_colors = {node: "#D3D3D3" for node in tree.nodes()}  # Початковий колір (сірий)
    for i, node in enumerate(visited_nodes):
        node_colors[node.id] = colors[i]

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500,
            node_color=[node_colors[node] for node in tree.nodes()])
    plt.title(title)
    plt.show()

def bfs_traversal(root):
    """Обхід у ширину (BFS) через чергу"""
    queue = deque([root])
    visited_nodes = []

    while queue:
        node = queue.popleft()
        visited_nodes.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited_nodes

def dfs_traversal(root):
    """Обхід у глибину (DFS) через стек"""
    stack = [root]
    visited_nodes = []

    while stack:
        node = stack.pop()
        visited_nodes.append(node)
        if node.right:  # Додаємо спочатку правого сина (щоб лівий був першим)
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited_nodes

# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Виконання обходів
bfs_nodes = bfs_traversal(root)
dfs_nodes = dfs_traversal(root)

# Візуалізація обходу BFS
draw_tree(root, bfs_nodes, "Обхід у ширину (BFS)")

# Візуалізація обходу DFS
draw_tree(root, dfs_nodes, "Обхід у глибину (DFS)")