import random

def simulate_dice_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[roll_sum] += 1

    #Обчислення ймовірностей у відсотках
    probabilities = {sum_value: (count / num_rolls) * 100 for sum_value, count in sum_counts.items()}
    return probabilities

num_rolls = int(input("Введіть кількість кидків двох кубиків: "))

simulated = simulate_dice_rolls(num_rolls)

print("Сума\tІмовірність (%)")
for sum_value in range(2, 13):
    print(f"{sum_value}\t{simulated[sum_value]:.2f}")
