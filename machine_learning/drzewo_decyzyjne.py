import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


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
    
    display_set(train_input, "Zbiór treningowy (input): ")
    display_set(train_class, "Zbiór treningowy (class): ")
    display_set(test_input, "Zbiór testowy (input): ")
    display_set(test_class, "Zbiór testowy (class): ")

    tree = DecisionTreeClassifier(random_state=282172)
    tree = tree.fit(train_input, train_class)

    plt.figure()
    plot_tree(tree, filled=True)
    plt.show()

    accuracy = tree.score(test_input, test_class)
    print(f"Dokładność klasyfikatora: {accuracy * 100:.2f}%")

    predictions = tree.predict(test_input)
    matrix = confusion_matrix(test_class, predictions, labels=['setosa', 'versicolor', 'virginica'])

    plt.figure()
    sns.heatmap(matrix, annot=True, cmap='Reds', xticklabels=['setosa', 'versicolor', 'virginica'], yticklabels=['setosa', 'versicolor', 'virginica'])
    plt.xlabel('Przewidywane etykiety')
    plt.ylabel('Prawdziwe etykiety')
    plt.title('Macierz błędów')
    plt.show()

    return


def display_set(set, str):
    print(str)
    print(set.to_string())

if __name__ == "__main__":
    main()