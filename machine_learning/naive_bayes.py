import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
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

    guassian = GaussianNB()
    guassian.fit(train_input, train_class)

    predictions = guassian.predict(test_input)
    accuracy = accuracy_score(test_class, predictions)
    print(f"Dokładność klasyfikatora Naive Bayes: {accuracy * 100:.2f}%")

    matrix = confusion_matrix(test_class, predictions, labels=['setosa', 'versicolor', 'virginica'])

    display_matrix(matrix, "Naive Bayes")

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