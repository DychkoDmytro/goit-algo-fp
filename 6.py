def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм вибирає страви, максимізуючи співвідношення калорій до вартості.
    """
    # Сортуємо елементи за співвідношенням калорій/вартість у порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    selected = []
    total_calories = 0
    remaining_budget = budget

    for item, data in sorted_items:
        if data["cost"] <= remaining_budget:
            selected.append(item)
            total_calories += data["calories"]
            remaining_budget -= data["cost"]

    return selected, total_calories


def dynamic_programming(items, budget):
    """
    Динамічне програмування для знаходження оптимального набору страв.
    Використовує підхід "Knapsack Problem".
    """
    # Перетворюємо словник у список для зручності
    food_list = list(items.items())
    n = len(food_list)
    
    # DP-масив: dp[i][w] - максимальна калорійність при використанні i предметів та бюджету w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення DP-таблиці
    for i in range(1, n + 1):
        item_name, data = food_list[i - 1]
        cost, calories = data["cost"], data["calories"]

        for w in range(budget + 1):
            if cost > w:
                dp[i][w] = dp[i - 1][w]  # Якщо не можемо взяти предмет, беремо попереднє значення
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)

    # Відновлення обраних предметів
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Якщо значення змінилося, значить, цей предмет було вибрано
            selected_items.append(food_list[i - 1][0])
            w -= food_list[i - 1][1]["cost"]

    selected_items.reverse()  # Оскільки ми додавали у зворотному порядку

    return selected_items, dp[n][budget]


# 📌 Тестування алгоритмів
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 60  # Приклад бюджету

# Виконання жадібного алгоритму
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм:\nОбрані страви: {greedy_result}\nЗагальна калорійність: {greedy_calories}")

# Виконання динамічного програмування
dp_result, dp_calories = dynamic_programming(items, budget)
print(f"\nДинамічне програмування:\nОбрані страви: {dp_result}\nЗагальна калорійність: {dp_calories}")