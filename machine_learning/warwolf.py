import random
import math
import matplotlib.pyplot as plt

def main():
    print("Hello world")

    hit = random.randint(50, 340) # Punkt do trafienia
    print(f"Cel jest w oddległości {hit}")

    boundry = 5 # granica błędu
    h = 100 # wysokość trebusza
    v = 50 # prędkość m/s

    g = 9.81 # Przyspieszenie ziemskie

    i = 0 # iteracje

    while True:
        alfa = int(input("Podaj kąt alfa: "))
        i += 1
        alfa_rad = math.radians(alfa)
        t = (v * math.sin(alfa_rad) + math.sqrt((v * math.sin(alfa_rad))**2 + 2 * g * h)) / g
        d = v * math.cos(alfa_rad) * t
        print(d)
        if hit-boundry <= d <= hit+boundry:
            print("Cel trafiony. Ilość prób: ", i)
            draw(alfa_rad, t, v, h, g)
            break
        else:
            print("Spróbuj ponownie")
    return

def draw(alfa_rad, t, v, h, g):
    time_points = [t * i / 100 for i in range(101)]
    x_points = [v * math.cos(alfa_rad) * t for t in time_points]
    y_points = [h + v * math.sin(alfa_rad) * t - 0.5 * g * t**2 for t in time_points]

    # Rysowanie trajektorii
    plt.plot(x_points, y_points)
    plt.title("Trajektoria lotu pocisku")
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.show()
    return

if __name__ == "__main__":
    main()