import pygad
import math
import numpy as np
import matplotlib.pyplot as plt

def endurance(x, y, z, u, v, w):
    return math.exp(-2 * (y - math.sin(x))**2) + math.sin(z * u) + math.cos(v * w)

def fitness_function(ga_instance, solution, solution_idx):
    x, y, z, u, v, w = solution
    return endurance(x, y, z, u, v, w)

gene_space = {"low": 0.0, "high": 1.0}

ga_instance = pygad.GA(
    num_generations=50,
    num_parents_mating=5,
    fitness_func=fitness_function,
    sol_per_pop=20,
    num_genes=6,
    init_range_low=0.0,
    init_range_high=1.0,
    parent_selection_type="sss",
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=20,
    gene_space=gene_space
)

ga_instance.run()

solution, solution_fitness, _ = ga_instance.best_solution()
print(f"Najlepszy chromosom: {solution}")
print(f"Maksymalna wytrzymałość: {solution_fitness}")

plt.plot(ga_instance.best_solutions_fitness)
plt.title("Proces optymalizacji (wartość fitness)")
plt.xlabel("Pokolenie")
plt.ylabel("Wartość fitness")
plt.show()
