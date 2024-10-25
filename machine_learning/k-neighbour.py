import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['variety'] = iris.target    
    df['variety'] = df['variety'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    train_set, test_set = train_test_split(df, train_size=0.7, random_state=282172)

    train_input = train_set.drop(columns=['variety'])
    train_class = train_set['variety']
    test_input = test_set.drop(columns=['variety'])
    test_class = test_set['variety']

    k_values = [3, 5, 11]

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(train_input, train_class)
    
        predictions = knn.predict(test_input)
        matrix = confusion_matrix(test_class, predictions, labels=['setosa', 'versicolor', 'virginica'])
        display_matrix(matrix, k)

        accuracy = accuracy_score(test_class, predictions)
        print(f"Dokładność klasyfikatora k-NN dla k={k}: {accuracy * 100:.2f}%")

    return


def display_matrix(m, k):
    plt.figure()
    sns.heatmap(m, annot=True, cmap='Reds', xticklabels=['setosa', 'versicolor', 'virginica'], yticklabels=['setosa', 'versicolor', 'virginica'])
    plt.xlabel('Przewidywane etykiety')
    plt.ylabel('Prawdziwe etykiety')
    plt.title(f'Macierz błędów dla {k}')
    plt.show()

if __name__ == "__main__":
    main()