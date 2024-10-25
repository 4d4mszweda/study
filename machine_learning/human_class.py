import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def main():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['variety'] = iris.target    
    df['variety'] = df['variety'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    train_set, test_set = train_test_split(df, train_size=0.7, random_state=282172)

    good_predictions = 0
    len = test_set.shape[0]

    for i in range(len):
        row = test_set.iloc[i]
        if classify_iris(row['sepal length (cm)'], row['sepal width (cm)'], row['petal length (cm)'], row['petal width (cm)']) == row['variety']:
            good_predictions += 1

    print("Good predictions: ", good_predictions)
    print("Accuracy: ", good_predictions/len*100, "%")

    # train_set_sorted = train_set.sort_values(by='variety')
    # print(train_set_sorted.to_string())

    return

def classify_iris(sl, sw, pl, pw):
    if pl < 3: # 1 - 2
        return "setosa"
    elif pl < 5: # 5.1 max versicolor && 4.9 min virginica
        return "versicolor"
    else:
        return "virginica"

if __name__ == "__main__":
    main()