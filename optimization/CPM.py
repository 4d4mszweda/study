# Implementacja metody ścieżki krytycznej, która dla podanego przez użytkownika zestawu zadań zbuduje sieć AA lub AN, 
# a następnie dla każdego zadania:
#  -> wyliczy najwcześniejszy oraz najpóźniejszy moment wykonywania zadania, 
#  -> poda ścieżkę krytyczną, 
#  -> poda harmonogram (wg najwcześniejszych czasów rozpoczęcia zadań 
#  -> poda długość harmonogramu.
class Task:
    def __init__(self, name, duration, predecessors=None):
        self.name = name
        self.duration = duration
        self.predecessors = predecessors if predecessors else []
        self.earliest_start = None
        self.latest_start = None



def main():
    return

def CPM():
    return

if __name__ == "__main__":
    main()