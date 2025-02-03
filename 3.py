import heapq

class Graph:
    def __init__(self):
        """Ініціалізуємо граф у вигляді adjacency list (списку суміжності)"""
        self.nodes = {}

    def add_edge(self, u, v, weight):
        """Додає ребро між вершинами u та v з вагою weight"""
        if u not in self.nodes:
            self.nodes[u] = {}
        if v not in self.nodes:
            self.nodes[v] = {}
        self.nodes[u][v] = weight
        self.nodes[v][u] = weight  # Граф неорієнтований

    def dijkstra(self, start):
        """Знаходить найкоротші шляхи з вершини start до всіх інших"""
        shortest_paths = {node: float('inf') for node in self.nodes}  # Початково всі відстані ∞
        shortest_paths[start] = 0  # Відстань до початкової вершини = 0
        priority_queue = [(0, start)]  # Бінарна купа (вага, вершина)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Якщо ми знайшли кращий шлях раніше, пропускаємо цей вузол
            if current_distance > shortest_paths[current_node]:
                continue

            # Оновлюємо відстані до сусідніх вузлів
            for neighbor, weight in self.nodes[current_node].items():
                distance = current_distance + weight
                if distance < shortest_paths[neighbor]:  # Якщо знайшли коротший шлях
                    shortest_paths[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_paths

# Тестовий приклад
graph = Graph()
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 8)
graph.add_edge("C", "E", 10)
graph.add_edge("D", "E", 2)
graph.add_edge("D", "F", 6)
graph.add_edge("E", "F", 3)

# Виконання алгоритму Дейкстри з вершини 'A'
start_node = "A"
shortest_paths = graph.dijkstra(start_node)

# Виведення результату
print(f"Найкоротші шляхи з вершини {start_node}:")
for node, distance in shortest_paths.items():
    print(f"Вершина {node}: {distance}")