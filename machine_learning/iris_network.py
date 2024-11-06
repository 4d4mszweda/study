import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def main():
    # Załaduj dane
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['variety'] = iris.target

    # Podziel dane na część testową i treningową
    train_set, test_set = train_test_split(df, train_size=0.7, random_state=282172)
    train_input = train_set.drop(columns=['variety'])
    train_class = train_set['variety']
    test_input = test_set.drop(columns=['variety'])
    test_class = test_set['variety']

    # Przeskaluj dane
    scaler = StandardScaler()
    train_input = scaler.fit_transform(train_input)
    test_input = scaler.transform(test_input)

    # Model 1: 4-neuronowa warstwa wejściowa, 1 ukryta warstwa z 2 neuronami
    model1 = MLPClassifier(hidden_layer_sizes=(2,), max_iter=1000, random_state=1)
    model1.fit(train_input, train_class)
    predictions1 = model1.predict(test_input)
    accuracy1 = accuracy_score(test_class, predictions1)
    print(f"\nModel 1 Accuracy: {accuracy1}\n")

    # Model 2: 4-neuronowa warstwa wejściowa, 1 ukryta warstwa z 3 neuronami
    model2 = MLPClassifier(hidden_layer_sizes=(3,), max_iter=1000, random_state=1)
    model2.fit(train_input, train_class)
    predictions2 = model2.predict(test_input)
    accuracy2 = accuracy_score(test_class, predictions2)
    print(f"\nModel 2 Accuracy: {accuracy2}\n")

    # Model 3: 4-neuronowa warstwa wejściowa, 2 ukryte warstwy z 3 neuronami każda
    model3 = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=1000, random_state=1)
    model3.fit(train_input, train_class)
    predictions3 = model3.predict(test_input)
    accuracy3 = accuracy_score(test_class, predictions3)
    print(f"\nModel 3 Accuracy: {accuracy3}\n")

    # Porównaj dokładności
    best_accuracy = max(accuracy1, accuracy2, accuracy3)
    print(f"\nNajlepsza dokładność: {best_accuracy}\n")

if __name__ == "__main__":
    main()