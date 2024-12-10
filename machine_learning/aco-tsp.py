import matplotlib.pyplot as plt
import random
import math
import time

from aco import AntColony


plt.style.use("dark_background")


COORDS = (
    (20, 52), (43, 50), (20, 84), (70, 65), (29, 90), (87, 83), (73, 23),
    (15, 10), (50, 30), (60, 70), (80, 20), (90, 40), (10, 60), (30, 80),
    (40, 90), (60, 10), (70, 30), (80, 50), (90, 70), (100, 90)
)


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


def calculate_total_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += math.sqrt((path[i][0] - path[i + 1][0]) ** 2 + (path[i][1] - path[i + 1][1]) ** 2)
    return total_distance

params = [
    {'ant_count': 200, 'alpha': 0.7, 'beta': 1.5, 'pheromone_evaporation_rate': 0.50, 'pheromone_constant': 800.0, 'iterations': 200},
    {'ant_count': 300, 'alpha': 0.5, 'beta': 1.2, 'pheromone_evaporation_rate': 0.40, 'pheromone_constant': 1000.0, 'iterations': 200},
    {'ant_count': 500, 'alpha': 1.0, 'beta': 2.0, 'pheromone_evaporation_rate': 0.30, 'pheromone_constant': 1500.0, 'iterations': 200},
    {'ant_count': 700, 'alpha': 1.0, 'beta': 2.0, 'pheromone_evaporation_rate': 0.30, 'pheromone_constant': 1500.0, 'iterations': 200},
]

plot_nodes()
start_time = time.time()

x = 3

colony = AntColony(COORDS, 
                    ant_count=params[x]['ant_count'], 
                    alpha=params[x]['alpha'], 
                    beta=params[x]['beta'], 
                    pheromone_evaporation_rate=params[x]['pheromone_evaporation_rate'], 
                    pheromone_constant=params[x]['pheromone_constant'], 
                    iterations=params[x]['iterations'])

optimal_nodes = colony.get_path()
total_distance = calculate_total_distance(optimal_nodes)

end_time = time.time()
elapsed_time = end_time - start_time

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )

plt.title(f"Ant Count: {params[x]['ant_count']}, Alpha: {params[x]['alpha']}, Beta: {params[x]['beta']}, Iterations: {params[x]['iterations']}\nTotal Distance: {total_distance:.2f}, Time: {elapsed_time:.2f} seconds")
plt.show()


# 1.1   14 sekund - 520 dys
# 1.2   14 sekund - 440 dys
# 1.3   14 sekund - 454 dys

# 2.1   21 sekund - 480 dys
# 2.2   21 sekund - 441 dys
# 2.3   21 sekund - 454 dys

# 3.1   35 sekund - 478 dys
# 3.2   35 sekund - 454 dys
# 3.3   35 sekund - 480 dys

# 4.1   50 sekund - 522 dys     