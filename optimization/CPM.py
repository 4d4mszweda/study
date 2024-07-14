# Implementacja metody ścieżki krytycznej, która dla podanego przez użytkownika zestawu zadań zbuduje sieć AA lub AN, 
# a następnie dla każdego zadania:
#  -> wyliczy najwcześniejszy oraz najpóźniejszy moment wykonywania zadania, 
#  -> poda ścieżkę krytyczną, 
#  -> poda harmonogram (wg najwcześniejszych czasów rozpoczęcia zadań 
#  -> poda długość harmonogramu.
import networkx as nx
import matplotlib.pyplot as plt

class Task:
    def __init__(self, name, duration, predecessors=None):
        self.name = name
        self.duration = duration
        self.predecessors = predecessors if predecessors else []

def critical_path(tasks):
    # Tworzenie grafu
    G = nx.DiGraph()

    # Dodawanie zadań do grafu
    for task in tasks:
        G.add_node(task.name, duration=task.duration)
        for pred in task.predecessors:
            G.add_edge(pred, task.name)

    # Znajdowanie najdłuższych ścieżek w grafie (CPM)
    critical_path = nx.dag_longest_path(G)

    # Obliczanie długości ścieżki krytycznej
    critical_path_duration = sum(G.nodes[task]["duration"] for task in critical_path)

    return critical_path, critical_path_duration, G

def draw_network(G):
    pos = nx.shell_layout(G)
    node_labels = {node: f"{node}\n({G.nodes[node]['duration']})" for node in G.nodes()}
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_color="lightblue", node_size=2000, font_size=10)
    plt.title("Activity on Arc Network")
    plt.show()

def main():
    tasks = [
        Task("Start", 0),
        Task("A", 3, ["Start"]),
        Task("B", 4, ["Start"]),
        Task("C", 2, ["A"]),
        Task("D", 5, ["A", "B"]),
        Task("End", 0, ["C", "D"])
    ]

    cp, cp_duration, G = critical_path(tasks)
    print("Critical Path:", cp)
    print("Total Duration of Critical Path:", cp_duration)
    draw_network(G)

if __name__ == "__main__":
    main()