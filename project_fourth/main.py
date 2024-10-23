import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас вузла
class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Додавання ребер для купи з використанням рекурсії
def add_heap_edges(graph: nx.DiGraph, i, heap, pos, x=0, y=0, layer=1):
    n = len(heap)
    if i >= n:
        return

    node: Node = heap[i]
    graph.add_node(node.id, color=node.color, label=node.val)
    
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    # Обчислення зміщення для лівого вузла
    if left_index < n:
        left_child = heap[left_index]
        graph.add_edge(node.id, left_child.id)
        l = x - 1 / (2 ** layer)
        pos[left_child.id] = (l, y - 1)
        add_heap_edges(graph, left_index, heap, pos, x=l, y=y - 1, layer=layer + 1)

    # Обчислення зміщення для правого вузла
    if right_index < n:
        right_child = heap[right_index]
        graph.add_edge(node.id, right_child.id)
        r = x + 1 / (2 ** layer)
        pos[right_child.id] = (r, y - 1)
        add_heap_edges(graph, right_index, heap, pos, x=r, y=y - 1, layer=layer + 1)

# Візуалізація купи
def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    add_heap_edges(tree, 0, heap, pos, x=0, y=0, layer=1)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, with_labels=True)
    plt.show()

# Створення мін-купи
heap = [Node(10), Node(60), Node(30), Node(10), Node(80), Node(20), Node(50), Node(90)]

# Відображення купи
draw_heap(heap)
