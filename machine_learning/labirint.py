import pygad
import numpy as np
import time
import matplotlib.pyplot as plt

labirynt = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

start = (1, 1)
end = (10, 10)

def fitness_function(ga_instance, solution, solution_idx):
    x, y = start
    steps = 0
    score = 0
    

    for move in solution:
        
        if move == 0:  # Góra
            x -= 1
        elif move == 1:  # Dół
            x += 1
        elif move == 2:  # Lewo
            y -= 1
        elif move == 3:  # Prawo
            y += 1

        if 0 <= x < labirynt.shape[0] and 0 <= y < labirynt.shape[1] and labirynt[x, y] == 0:
            steps += 1
            

            score += 1 / (abs(end[0] - x) + abs(end[1] - y) + 1)
            if (x, y) == end:
                score += 100
                break
        else:
            score -= 10
            break

    return score

gene_space = [0, 1, 2, 3]  # Możliwe ruchy: góra, dół, lewo, prawo

ga_instance = pygad.GA(
    num_generations=200,
    num_parents_mating=10,
    fitness_func=fitness_function,
    sol_per_pop=100,
    num_genes=30,
    init_range_low=0,
    init_range_high=3,
    mutation_type="random",
    mutation_percent_genes=15,
    gene_space=gene_space,
    stop_criteria=["reach_100"]
)

def plot_labirynt(labirynt, path=None):
    plt.figure(figsize=(10, 10))
    plt.imshow(labirynt, cmap='Blues')

    if path:
        for (x, y) in path:
            plt.plot(y, x, 'ro')

    plt.title("Labirynt")
    plt.show()

def get_path_from_solution(solution, start):
    x, y = start
    path = [(x, y)]
    for move in solution:
        if move == 0:  # Góra
            x -= 1
        elif move == 1:  # Dół
            x += 1
        elif move == 2:  # Lewo
            y -= 1
        elif move == 3:  # Prawo
            y += 1
        path.append((x, y))
    return path

start_time = time.time()
ga_instance.run()
end_time = time.time()

solution, solution_fitness, _ = ga_instance.best_solution()
print(f"Najlepsza ścieżka: {solution}")
print(f"Dopasowanie: {solution_fitness}")
print(f"Czas wykonania: {end_time - start_time:.2f} s")

ga_instance.plot_fitness(title="Proces optymalizacji fitness")

plot_labirynt(labirynt)
plot_labirynt(labirynt, get_path_from_solution(solution, start))