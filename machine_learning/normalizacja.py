import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def main():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target

    X_sepal = X[['sepal length (cm)', 'sepal width (cm)']]

    # Oryginalne
    plot_iris_sepal(X_sepal, y, 'Oryginalne dane Iris')

    # Min- Max
    scaler_minmax = MinMaxScaler()
    X_sepal_minmax = pd.DataFrame(scaler_minmax.fit_transform(X_sepal), columns=X_sepal.columns)
    plot_iris_sepal(X_sepal_minmax, y, 'Znormalizowane dane Iris (Min-Max)')

    # Z-Score
    scaler_zscore = StandardScaler()
    X_sepal_zscore = pd.DataFrame(scaler_zscore.fit_transform(X_sepal), columns=X_sepal.columns)
    plot_iris_sepal(X_sepal_zscore, y, 'Zeskalowane dane Iris (Z-Score)')

def plot_iris_sepal(X, y, title):
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap='viridis', edgecolor='k')
    plt.colorbar(scatter, label='Typ irysa (0=Setosa, 1=Versicolor, 2=Virginica)')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    main()