import math
import random
import matplotlib.pyplot as plt

# Parametry fizyczne
v0 = 50  # prędkość początkowa w m/s
h = 100  # wysokość trebusza w metrach
g = 9.81  # przyspieszenie grawitacyjne

# Funkcja do obliczania odległości i czasu lotu na podstawie kąta strzału
def calculate_trajectory(angle_degrees):
    angle_radians = math.radians(angle_degrees)  # konwersja kąta na radiany
    vertical_velocity = v0 * math.sin(angle_radians)  # składowa pionowa prędkości
    horizontal_velocity = v0 * math.cos(angle_radians)  # składowa pozioma prędkości
    
    # Obliczenie czasu lotu
    time_of_flight = (vertical_velocity + math.sqrt(vertical_velocity**2 + 2 * g * h)) / g
    
    # Obliczenie trajektorii: lista czasów i położenia x, y
    t_values = [t * time_of_flight / 1000 for t in range(1001)]  # podziel czas na 1000 kroków
    x_values = [horizontal_velocity * t for t in t_values]  # pozycja x
    y_values = [h + vertical_velocity * t - 0.5 * g * t**2 for t in t_values]  # pozycja y
    
    return x_values, y_values, x_values[-1]  # zwróć trajektorię i końcową odległość

# Funkcja gry
def trebuchet_game():
    # Wybór losowego celu
    target_distance = random.randint(50, 340)
    print(f"Cel znajduje się w odległości: {target_distance} metrów.")

    attempts = 0  # licznik prób

    while True:
        # Pobieranie kąta strzału od użytkownika
        try:
            angle = float(input("Podaj kąt strzału (w stopniach): "))
        except ValueError:
            print("Błędny format. Wprowadź liczbę.")
            continue

        # Obliczenie trajektorii i końcowej odległości
        x_values, y_values, shot_distance = calculate_trajectory(angle)
        attempts += 1

        print(f"Pocisk przeleciał: {shot_distance:.2f} metrów.")

        # Sprawdzenie, czy pocisk trafił w cel z marginesem błędu 5 metrów
        if abs(shot_distance - target_distance) <= 5:
            print("Cel trafiony!")
            print(f"Liczba prób: {attempts}")
            break
        else:
            print("Chybiony! Spróbuj ponownie.")
        
        # Wizualizacja trajektorii i celu
        visualize_trajectory(x_values, y_values, target_distance, shot_distance)

# Funkcja do wizualizacji trajektorii
def visualize_trajectory(x_values, y_values, target_distance, shot_distance):
    plt.figure(figsize=(10, 5))
    
    # Rysowanie trajektorii pocisku
    plt.plot(x_values, y_values, label="Trajektoria pocisku")
    
    # Zaznaczenie celu
    plt.axvline(x=target_distance, color='r', linestyle='--', label=f"Cel: {target_distance} m")
    
    # Zaznaczenie końcowego położenia pocisku
    plt.scatter([shot_distance], [0], color='b', label=f"Upadek pocisku: {shot_distance:.2f} m")
    
    # Ustawienia wykresu
    plt.xlim(0, max(x_values) + 50)
    plt.ylim(0, max(y_values) + 50)
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.title(f"Trajektoria lotu przy kącie {math.degrees(math.atan2(y_values[1], x_values[1])):.2f}°")
    plt.legend()
    plt.grid(True)
    plt.show()

# Uruchomienie gry
if __name__ == "__main__":
    trebuchet_game()
