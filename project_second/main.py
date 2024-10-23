import matplotlib.pyplot as plt
import numpy as np

def draw_line(start, end, ax):
    ax.plot([start[0], end[0]], [start[1], end[1]], color='green')

def calculate_new_endpoints(start, end, length):
    direction = np.array([end[0] - start[0], end[1] - start[1]])
    direction = direction / np.linalg.norm(direction)

    rotation_matrix_left = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
                                     [np.sin(np.pi/4), np.cos(np.pi/4)]])

    rotation_matrix_right = np.array([[np.cos(-np.pi/4), -np.sin(-np.pi/4)],
                                      [np.sin(-np.pi/4), np.cos(-np.pi/4)]])

    new_direction_left = np.dot(rotation_matrix_left, direction) * length
    new_direction_right = np.dot(rotation_matrix_right, direction) * length

    new_end_left = [end[0] + new_direction_left[0], end[1] + new_direction_left[1]]
    new_end_right = [end[0] + new_direction_right[0], end[1] + new_direction_right[1]]
    
    return new_end_left, new_end_right

def draw_tree(start, end, level, ax):
    if level == 0:
        return

    draw_line(start, end, ax)

    length = np.linalg.norm([end[0] - start[0], end[1] - start[1]]) / 1.3
    new_end_left, new_end_right = calculate_new_endpoints(start, end, length)

    draw_tree(end, new_end_left, level - 1, ax)
    draw_tree(end, new_end_right, level - 1, ax)

def main():
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()

    start = [0, 0]
    end = [0, 1]

    level = int(input("Введіть рівень рекурсії: "))

    draw_tree(start, end, level, ax)

    plt.show()

main()
