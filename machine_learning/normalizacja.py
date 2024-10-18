import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Wczytanie danych Iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Wybór tylko kolumn: sepal length i sepal width
X_sepal = X[['sepal length (cm)', 'sepal width (cm)']]

# Tworzenie wykresu dla oryginalnych danych
def plot_iris_sepal(X, y, title):
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap='viridis', edgecolor='k')
    plt.colorbar(scatter, label='Typ irysa (0=Setosa, 1=Versicolor, 2=Virginica)')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title(title)
    plt.show()

# Dane oryginalne
plot_iris_sepal(X_sepal, y, 'Oryginalne dane Iris')

# Normalizacja (Min-Max scaling)
scaler_minmax = MinMaxScaler()
X_sepal_minmax = pd.DataFrame(scaler_minmax.fit_transform(X_sepal), columns=X_sepal.columns)

plot_iris_sepal(X_sepal_minmax, y, 'Znormalizowane dane Iris (Min-Max)')

# Standaryzacja (Z-score scaling)
scaler_zscore = StandardScaler()
X_sepal_zscore = pd.DataFrame(scaler_zscore.fit_transform(X_sepal), columns=X_sepal.columns)

plot_iris_sepal(X_sepal_zscore, y, 'Zeskalowane dane Iris (Z-Score)')

# Obliczenie statystyk dla danych oryginalnych, znormalizowanych i zeskalowanych
def print_statistics(X, title):
    print(f"\nStatystyki dla {title}:")
    print(f"Min:\n{X.min()}")
    print(f"Max:\n{X.max()}")
    print(f"Mean:\n{X.mean()}")
    print(f"Standard Deviation:\n{X.std()}")

print_statistics(X_sepal, 'oryginalnych danych')
print_statistics(X_sepal_minmax, 'znormalizowanych danych (Min-Max)')
print_statistics(X_sepal_zscore, 'zeskalowanych danych (Z-Score)')
