import random
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_dice_simulation(num_rolls=100000):
    """
    Симуляція кидків двох кубиків та обчислення ймовірностей сум.
    """
    sum_counts = {i: 0 for i in range(2, 13)}  # Зберігаємо кількість випадків для кожної суми

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)  # Два кубики
        sum_counts[roll_sum] += 1  # Підраховуємо кількість

    # Розрахунок ймовірностей у відсотках
    sum_probabilities = {key: (value / num_rolls) * 100 for key, value in sum_counts.items()}
    
    return sum_counts, sum_probabilities

def plot_results(monte_carlo_probs):
    """
    Побудова графіка порівняння аналітичних і експериментальних ймовірностей.
    """
    analytical_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
        8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    sums = list(monte_carlo_probs.keys())
    monte_carlo_values = list(monte_carlo_probs.values())
    analytical_values = [analytical_probs[sum_value] for sum_value in sums]

    plt.figure(figsize=(10, 5))
    plt.bar(sums, monte_carlo_values, color="skyblue", label="Монте-Карло")
    plt.plot(sums, analytical_values, marker="o", color="red", linestyle="dashed", label="Аналітичні")

    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність (%)")
    plt.title("Порівняння ймовірностей Монте-Карло та аналітичних значень")
    plt.xticks(range(2, 13))
    plt.legend()
    plt.grid()
    plt.show()

# Запуск симуляції
num_rolls = 100000
sum_counts, sum_probs = monte_carlo_dice_simulation(num_rolls)

# Виведення результатів у вигляді таблиці
df = pd.DataFrame({
    "Сума": list(sum_probs.keys()),
    "Ймовірність Монте-Карло (%)": list(sum_probs.values())
})
df["Аналітична ймовірність (%)"] = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

import ace_tools as tools
tools.display_dataframe_to_user(name="Ймовірності сум кубиків", dataframe=df)

# Побудова графіка
plot_results(sum_probs)