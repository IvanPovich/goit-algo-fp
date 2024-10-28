from binary_tree import *
from collections import deque
import matplotlib.colors as mcolors

def bfs(tree_root):
    queue = deque([tree_root])
    visited_colors = {}
    color_list = list(mcolors.LinearSegmentedColormap.from_list("", ["#003366", "#66c2ff"])(range(256)))  # Градієнт від темного синього до світло-блакитного
    color_index = 0

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    while queue:
        node = queue.popleft()
        visited_colors[node.id] = color_list[color_index]
        color_index = min(color_index + 42, 255)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    draw_tree(tree, pos, visited_colors, "Обхід в ширину")

def dfs(tree_root):
    stack = [tree_root]
    visited_colors = {}
    color_list = list(mcolors.LinearSegmentedColormap.from_list("", ["#660000", "#ff6666"])(range(256)))  # Градієнт від темного червоного до світло-рожевого
    color_index = 0

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    while stack:
        node = stack.pop()
        visited_colors[node.id] = color_list[color_index]
        color_index = min(color_index + 42, 255)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    draw_tree(tree, pos, visited_colors, "Обхід в глибину")
