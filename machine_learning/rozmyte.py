# Użyjemy paczki simpful, by stworzyć prosty kontroler rozmyty do obliczania napiwków (przykład był na wykładzie).
# a) Poczytaj o paczce simpful np. tutaj:
# • https://pypi.org/project/simpful/
# • https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html
# • https://www.researchgate.net/publication/346395808_Simpful_A_User-Friendly_Python_Library_for_Fuzzy_Logic
# Zwróć uwagę na wstawki kodu i sposób tworzenia kontrolerów (zmienne, reguły, wyostrzanie).
# b) Zainstaluj paczkę i skopiuj z wybranej strony kod tworzący system do dawania napiwków (3 zmienne lingwistyczne, 3 reguły).
# c) Wyświetl wykresy zmiennych lingwistycznych.
# d) Przetestuj działanie kontrolera. Daj kilka danych (liczby dla jedzenia i obsługi) i wyświetl jaki napiwek (0-30%) proponuje system dla tych inputów.

import simpful as sf
import matplotlib.pyplot as plt

FS = sf.FuzzySystem()

S_1 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=0, b=0, c=2, d=4), term="bad")
S_2 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=2, b=4, c=6, d=8), term="average")
S_3 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=6, b=8, c=10, d=10), term="good")
FS.add_linguistic_variable("Food", sf.LinguisticVariable([S_1, S_2, S_3], concept="Food quality", universe_of_discourse=[0,10]))

S_4 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=0, b=0, c=2, d=4), term="poor")
S_5 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=2, b=4, c=6, d=8), term="acceptable")
S_6 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=6, b=8, c=10, d=10), term="excellent")
FS.add_linguistic_variable("Service", sf.LinguisticVariable([S_4, S_5, S_6], concept="Service quality", universe_of_discourse=[0,10]))

S_7 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=0, b=0, c=5, d=10), term="low")
S_8 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=5, b=10, c=15, d=20), term="medium")
S_9 = sf.FuzzySet(function=sf.Trapezoidal_MF(a=15, b=20, c=25, d=30), term="high")
FS.add_linguistic_variable("Tip", sf.LinguisticVariable([S_7, S_8, S_9], concept="Tip amount", universe_of_discourse=[0,30]))

R1 = "IF (Food IS bad) OR (Service IS poor) THEN (Tip IS low)"
R2 = "IF (Food IS average) THEN (Tip IS medium)"
R3 = "IF (Food IS good) AND (Service IS excellent) THEN (Tip IS high)"
FS.add_rules([R1, R2, R3])

FS.plot_variable("Food")
FS.plot_variable("Service")
FS.plot_variable("Tip")
plt.show()

def get_tip(food_quality, service_quality):
    FS.set_variable("Food", food_quality)
    FS.set_variable("Service", service_quality)
    tip = FS.inference()["Tip"]
    return tip

print("Tip for food quality 3 and service quality 7:", get_tip(3, 7))
print("Tip for food quality 8 and service quality 9:", get_tip(8, 9))
print("Tip for food quality 5 and service quality 5:", get_tip(5, 5))