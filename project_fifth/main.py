from binary_tree import *
from bfs_dfs import *


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходу в ширину
bfs(root)

# Відображення обходу в глибину
dfs(root)
