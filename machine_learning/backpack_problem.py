import pygad
import numpy as np
import time
import matplotlib.pyplot as plt

# Definicja problemu plecakowego
items = [
    {"name": "zegar", "value": 100, "weight": 7},
    {"name": "obraz-pejzaz", "value": 300, "weight": 7},
    {"name": "obraz-portret", "value": 200, "weight": 6},
    {"name": "radio", "value": 40, "weight": 2},
    {"name": "laptop", "value": 500, "weight": 5},
    {"name": "lampka nocna", "value": 70, "weight": 6},
    {"name": "srebne sztucce", "value": 100, "weight": 1},
    {"name": "porcelana", "value": 250, "weight": 3},
    {"name": "figura z brazu", "value": 300, "weight": 10},
    {"name": "skorzana torebka", "value": 280, "weight": 3},
    {"name": "odkurzacz", "value": 300, "weight": 15},
]
limit = 25
best_value = 1630


def fitness_function(ga_instance, solution, solution_idx):
    total_weight = 0
    total_value = 0

    for idx, selected in enumerate(solution):
        if selected == 1:
            total_weight += items[idx]["weight"]
            total_value += items[idx]["value"]

    if total_weight > limit:
        return 0
    return total_value


def run_genetic_algorithm():
    ga_instance = pygad.GA(
        gene_space=[0, 1],
        num_generations=100,
        num_parents_mating=5,
        fitness_func=fitness_function,
        sol_per_pop=20,
        num_genes=len(items),
        parent_selection_type="sss",
        keep_parents=2,
        crossover_type="single_point",
        mutation_type="random",
        mutation_percent_genes=8,
        stop_criteria=["reach_1630"],
    )

    start_time = time.time()
    ga_instance.run()
    end_time = time.time()

    solution, solution_fitness, _ = ga_instance.best_solution()

    solution_weight = sum(
        [items[i]["weight"] for i in range(len(items)) if solution[i] == 1]
    )

    return {
        "solution": solution,
        "fitness": solution_fitness,
        "weight": solution_weight,
        "time": end_time - start_time,
        "ga_instance": ga_instance,
    }


# Uruchomienie algorytmu dla analizy
results = []
success_count = 0
total_time = 0

for i in range(10):
    result = run_genetic_algorithm()
    results.append(result)

    if result["fitness"] == best_value:
        success_count += 1
        total_time += result["time"]

# Wyświetlanie wyników
print(f"Liczba sukcesów (wartość {best_value}): {success_count}/10")
if success_count > 0:
    print(
        f"Średni czas znalezienia najlepszego rozwiązania: {total_time / success_count:.2f} sekund"
    )
else:
    print("Nie znaleziono najlepszego rozwiązania w żadnej próbie.")

# Wykres optymalizacji (dla pierwszego uruchomienia)
first_run = results[0]["ga_instance"]
plt.plot(first_run.best_solutions_fitness)
plt.title("Proces optymalizacji (wartość fitness)")
plt.xlabel("Pokolenie")
plt.ylabel("Wartość fitness")
plt.show()

# Najlepsze rozwiązanie z ostatniej próby
best_solution = results[-1]["solution"]
best_items = [items[i]["name"] for i in range(len(items)) if best_solution[i] == 1]
print("Przedmioty do zabrania:", best_items)
print("Wartość plecaka:", results[-1]["fitness"])
print("Waga plecaka:", results[-1]["weight"])
