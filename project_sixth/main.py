from Foot import Food
from algo import greedy_algorithm, dynamic_programming
items_data = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

items = [Food(name, data["cost"], data["calories"]) for name, data in items_data.items()]

budget = 100

greedy_calories, greedy_selection = greedy_algorithm(items, budget)
print("\nЖадібний алгоритм:")
print("Максимальні калорії:", greedy_calories)
print("Вибрані страви:", greedy_selection)

dp_calories, dp_selection = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Максимальні калорії:", dp_calories)
print("Вибрані страви:", dp_selection)
