import random
import matplotlib.pyplot as plt
import networkx as nx
"""
Код создает граф n*n размера где каждая вершина имеет 1-2 дуги(Т.е ненавправленный связный граф)
Для n=3/4 скорость неплоха
Однако для n>=5 создание такого графа остается маловероятным
"""

# Основная функция для создания графа
def create_graph(n, n_step):
    G = nx.Graph()
    nodes = [i for i in range(n)]

    # Задаём координаты узлов в виде сетки
    pos = {}
    index = 0
    for y in range(n_step):
        for x in range(n_step):
            pos[index] = (x, y)
            index += 1

    # Добавляем узлы в граф
    G.add_nodes_from(nodes)

    # Словарь для хранения степеней вершин
    degrees = {i: 0 for i in range(n)}

    # Повторяем, пока граф не станет связным
    while True:
        edges = []
        # Сбрасываем степени перед новой попыткой
        for i in range(n):
            degrees[i] = 0

        # Шаг 1: Создаём минимальную связную структуру (цепочку или дерево)
        for i in range(n - 1):
            if (i + 1) % n_step != 0:  # Не на правой границе
                edges.append((i, i + 1))  # Горизонтальное ребро
                degrees[i] += 1
                degrees[i + 1] += 1
            else:
                break  # Прерываем, чтобы добавить вертикальные связи позже

        # Добавляем вертикальные связи для связности
        for i in range(n_step - 1):
            edges.append((i * n_step, (i + 1) * n_step))  # Вертикальные рёбра в первом столбце
            degrees[i * n_step] += 1
            degrees[(i + 1) * n_step] += 1

        # Шаг 2: Добавляем дополнительные рёбра, чтобы довести степень до 1 или 2
        for i in range(n):
            if degrees[i] >= 2:  # Пропускаем, если степень уже 2
                continue

            # Возможные соседи: справа (i+1) или снизу (i+n_step)
            possible_neighbors = []
            if (i + 1) % n_step != 0 and (i + 1) < n:  # Не на правой границе
                if degrees[i + 1] < 2:
                    possible_neighbors.append(i + 1)
            if i + n_step < n:  # Не на нижней границе
                if degrees[i + n_step] < 2:
                    possible_neighbors.append(i + n_step)

            # Добавляем случайное ребро, если есть доступные соседи
            if possible_neighbors:
                neighbor = random.choice(possible_neighbors)
                edges.append((i, neighbor))
                degrees[i] += 1
                degrees[neighbor] += 1

        # Добавляем рёбра в граф
        G.add_edges_from(edges)

        # Проверяем связность
        if nx.is_connected(G):
            print("Граф связный")
            return G, pos, edges, degrees  # Возвращаем граф и степени
        else:
            print("Граф не связный, перезапуск...")
            G.remove_edges_from(edges)  # Удаляем рёбра и пробуем снова


# Параметры графа
n = 9  # Размер графа
n_step = int(n ** 0.5)  # Размер шага для сетки (5 для n=25)

# Создаём граф
G, pos, edges, degrees_dict = create_graph(n, n_step)

# Рисуем граф
nx.draw(G, pos=pos, with_labels=True, font_weight='bold', node_color='lightblue', node_size=200)

# Показываем граф
plt.show()

# Проверяем степени вершин
degrees = [G.degree[node] for node in G.nodes()]
print("Степени вершин (из NetworkX):", degrees)
print("Степени вершин (из словаря):", [degrees_dict[i] for i in range(n)])