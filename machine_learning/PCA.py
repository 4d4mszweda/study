import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D

def pca_visualization():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)

    pca = PCA()
    X_pca = pca.fit_transform(X)

    explained_variance_ratio = np.cumsum(pca.explained_variance_ratio_)

    # Znalezienie minimalnej liczby wymiarów, aby zachować przynajmniej 95% wariancji
    num_components = np.argmax(explained_variance_ratio >= 0.95) + 1

    print(f"Liczba komponentów potrzebna do zachowania 95% wariancji: {num_components}")

    for i, variance in enumerate(pca.explained_variance_ratio_):
        print(f"Główna składowa {i+1}: {variance:.2%} wariancji")

    # Redukcja danych do odpowiedniej liczby wymiarów
    X_reduced = X_pca[:, :num_components]

    if num_components == 2:
        plt.figure(figsize=(8,6))
        plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=iris.target, cmap='viridis', edgecolor='k')
        plt.colorbar(label='Typ irysa (0=Setosa, 1=Versicolor, 2=Virginica)')
        plt.xlabel('Pierwsza główna składowa')
        plt.ylabel('Druga główna składowa')
        plt.title('Dane Iris zredukowane do 2 wymiarów (PCA)')
        plt.show()

    elif num_components == 3:
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], 
                             c=iris.target, cmap='viridis', edgecolor='k')
        ax.set_xlabel('Pierwsza główna składowa')
        ax.set_ylabel('Druga główna składowa')
        ax.set_zlabel('Trzecia główna składowa')
        plt.title('Dane Iris zredukowane do 3 wymiarów (PCA)')
        plt.colorbar(scatter, label='Typ irysa (0=Setosa, 1=Versicolor, 2=Virginica)')
        plt.show()
    else:
        print("Zbyt wiele wymiarów do wyświetlenia na wykresie.")

pca_visualization()
