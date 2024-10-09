import datetime
import math

def calculate_biorhythm(days_lived, cycle_length):
    return math.sin(2 * math.pi * days_lived / cycle_length)

def main():
    # Get user input
    name = input("Podaj swoje imię: ")
    year = int(input("Podaj rok urodzenia (YYYY): "))
    month = int(input("Podaj miesiąc urodzenia (MM): "))
    day = int(input("Podaj dzień urodzenia (DD): "))

    # Calculate days lived
    birthdate = datetime.date(year, month, day)
    today = datetime.date.today()
    days_lived = (today - birthdate).days

    # Calculate biorhythms
    physical = calculate_biorhythm(days_lived, 23)
    emotional = calculate_biorhythm(days_lived, 28)
    intellectual = calculate_biorhythm(days_lived, 33)

    # Print results
    print(f"Witaj, {name}!")
    print(f"Dzisiaj jest {days_lived}-ty dzień Twojego życia.")
    print(f"Twój fizyczny biorytm: {physical:.2f}")
    print(f"Twój emocjonalny biorytm: {emotional:.2f}")
    print(f"Twój intelektualny biorytm: {intellectual:.2f}")

    # Check biorhythm levels and provide messages
    def check_biorhythm(biorhythm, cycle_length, name):
        if biorhythm > 0.5:
            print(f"Gratulacje, {name}! Masz wysoki wynik biorytmu!")
        elif biorhythm < -0.5:
            print(f"Nie martw się, {name}. Masz niski wynik biorytmu.")
            next_day_biorhythm = calculate_biorhythm(days_lived + 1, cycle_length)
            if next_day_biorhythm > biorhythm:
                print("Nie martw się. Jutro będzie lepiej!")

    check_biorhythm(physical, 23, "fizyczny")
    check_biorhythm(emotional, 28, "emocjonalny")
    check_biorhythm(intellectual, 33, "intelektualny")

if __name__ == "__main__":
    main()