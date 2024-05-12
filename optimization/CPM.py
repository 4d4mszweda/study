# Implementacja metody ścieżki krytycznej, która dla podanego przez użytkownika zestawu zadań zbuduje sieć AA lub AN, 
# a następnie dla każdego zadania:
#  -> wyliczy najwcześniejszy oraz najpóźniejszy moment wykonywania zadania, 
#  -> poda ścieżkę krytyczną, 
#  -> poda harmonogram (wg najwcześniejszych czasów rozpoczęcia zadań 
#  -> poda długość harmonogramu.

import networkx as nx
import matplotlib.pyplot as plt

class Task:
    def __init__(self, id, duration, dependencies):
        self.id = id
        self.duration = duration
        self.dependencies = dependencies
        self.earliest_start = 0
        self.latest_start = 0

class Project:
    def __init__(self):
        self.tasks = {}

    def add_task(self, id, duration, dependencies):
        self.tasks[id] = Task(id, duration, dependencies)

    def calculate_earliest_and_latest_start_times(self):
        for task in self.tasks.values():
            task.earliest_start = max([self.tasks[id].earliest_start + self.tasks[id].duration for id in task.dependencies], default=0)
        for task in reversed(list(self.tasks.values())):
            task.latest_start = min([self.tasks[id].latest_start - task.duration for id in self.tasks if task.id in self.tasks[id].dependencies], default=task.earliest_start)

    def find_critical_path(self):
        self.calculate_earliest_and_latest_start_times()
        return [task for task in self.tasks.values() if task.earliest_start == task.latest_start]

    def schedule(self):
        self.calculate_earliest_and_latest_start_times()
        return sorted(self.tasks.values(), key=lambda task: task.earliest_start)

    def get_schedule_length(self):
        return max([task.earliest_start + task.duration for task in self.tasks.values()])

    def visualize(self):
        G = nx.DiGraph()
        for task in self.tasks.values():
            G.add_node(task.id)
            for dependency in task.dependencies:
                G.add_edge(dependency, task.id)
        pos = nx.spring_layout(G, k=2)
        nx.draw(G, pos, with_labels=True)
        plt.show()


def main():
    project = Project()
    project.add_task('Z1', 3, [])
    project.add_task('Z2', 8, [])
    project.add_task('Z3', 2, [])
    project.add_task('Z4', 2, ['Z1'])
    project.add_task('Z5', 4, ['Z1'])
    project.add_task('Z6', 6, ['Z3'])
    project.add_task('Z7', 9, ['Z3'])
    project.add_task('Z8', 2, ['Z4'])
    project.add_task('Z9', 1, ['Z5', 'Z2', 'Z6'])
    project.add_task('Z10', 2, ['Z5', 'Z2', 'Z6'])
    project.add_task('Z11', 1, ['Z7'])
    project.add_task('Z12', 2, ['Z7'])
    project.add_task('Z13', 6, ['Z8', 'Z9'])
    project.add_task('Z14', 5, ['Z10', 'Z11'])
    project.add_task('Z15', 9, ['Z10', 'Z11'])
    project.add_task('Z16', 6, ['Z10', 'Z11'])
    project.add_task('Z17', 2, ['Z12'])
    project.add_task('Z18', 5, ['Z13', 'Z14'])
    project.add_task('Z19', 3, ['Z16', 'Z17'])

    project.calculate_earliest_and_latest_start_times()

    print("Critical path:")
    for task in project.find_critical_path():
        print(task.id, "earliest start:", task.earliest_start, "latest start:", task.latest_start)

    print("Schedule:")
    for task in project.schedule():
        print(f"Task {task.id} starts at {task.earliest_start}")

    print("Schedule length:", project.get_schedule_length())

    project.visualize()

if __name__ == "__main__":
    main()