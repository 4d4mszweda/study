import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the diabetes dataset
df = pd.read_csv('diabetes.csv') 

# Split the dataset into training (70%) and testing (30%) sets
train_set, test_set = train_test_split(df, train_size=0.7, random_state=282172)

train_input = train_set.drop(columns=['class'])
train_class = train_set['class']
test_input = test_set.drop(columns=['class'])
test_class = test_set['class']

# mlp = MLPClassifier(hidden_layer_sizes=(6, 3), activation='relu', max_iter=500, random_state=42)

activations = ['identity', 'logistic', 'tanh', 'relu']
results = {}

for activation in activations:
    mlp = MLPClassifier(hidden_layer_sizes=(6, 3), activation=activation, max_iter=500, random_state=42)
    mlp.fit(train_input, train_class)
    y_pred = mlp.predict(test_input)
    accuracy = accuracy_score(test_class, y_pred)
    conf_matrix = confusion_matrix(test_class, y_pred)
    results[activation] = (accuracy, conf_matrix)

for activation, (accuracy, conf_matrix) in results.items():
    print(f"Activation: {activation}")
    print(f"Accuracy: {accuracy}")
    print(f"Confusion Matrix:\n{conf_matrix}\n")

# FN są gorsze