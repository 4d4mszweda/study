import math
from datetime import datetime

def main():
    # Pobranie danych od użytkownika
    name, birth_date = get_user_data()

    # Obliczenie fal biorhytmów
    physical_biorhythm = calculate_biorhythm(birth_date, 23)
    emotional_biorhythm = calculate_biorhythm(birth_date, 28)
    intellectual_biorhythm = calculate_biorhythm(birth_date, 33)

    # Wyświetlenie informacji o osobie
    display_biorhythm_info(name, birth_date, "Hi", [physical_biorhythm, emotional_biorhythm, intellectual_biorhythm])


def calculate_biorhythm(birth_date, cycle_length):
    """Oblicza wartość sinusoidalną cyklu biorytmu."""
    days_diff = (datetime.today() - birth_date).days
    return math.sin((2 * math.pi / cycle_length) * days_diff)


def display_biorhythm_info(name, birth_date, greeting, biorhythms):
    """Wyświetla dane osoby oraz wyniki biorytmu."""
    biorhythm_labels = ["Physical", "Emotional", "Intellectual"]

    print()
    print(greeting)
    print(f"Name: {name}")
    print(f"Birthday: {birth_date.strftime('%Y-%m-%d')}\n")

    for label, value in zip(biorhythm_labels, biorhythms):
        print(f"{label}: {value:.2f}")
        interpret_biorhythm(value)
        print()


def interpret_biorhythm(value):
    """Interpretuje wartość biorytmu i wyświetla odpowiednią wiadomość."""
    if value > 0.5:
        print("Congratulations on a high result!")
    elif value < -0.5:
        print("Everyone has bad days. Right?")
        # Można tutaj dodać bardziej zaawansowaną logikę na przyszłe dni.


def get_user_data():
    """Pobiera dane od użytkownika."""
    name = input("Name: ")
    year = int(input("Birth year: "))
    month = int(input("Birth month (number): "))
    day = int(input("Birth day: "))
    birth_date = datetime(year, month, day)
    return name, birth_date


if __name__ == "__main__":
    main()
