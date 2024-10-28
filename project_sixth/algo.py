def greedy_algorithm(items, budget):
    items = sorted(items, key=lambda x: x.ratio, reverse=True)
    total_calories = 0
    selected_items = []

    for item in items:
        if budget >= item.cost:
            budget -= item.cost
            total_calories += item.calories
            selected_items.append(item.name)
    
    return total_calories, selected_items

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    keep = [[False for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[i - 1]
        for b in range(1, budget + 1):
            if item.cost <= b:
                if dp[i - 1][b] < dp[i - 1][b - item.cost] + item.calories:
                    dp[i][b] = dp[i - 1][b - item.cost] + item.calories
                    keep[i][b] = True
                else:
                    dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = dp[i - 1][b]

    total_calories = dp[n][budget]
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if keep[i][b]:
            selected_items.append(items[i - 1].name)
            b -= items[i - 1].cost

    return total_calories, selected_items
