import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Prompt to po prostu kopiuj wklej polecenie 

# Wczytanie danych iris
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', 
                 header=None, 
                 names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'variety'])

# Oryginalny wykres
def plot_iris(data, title):
    sns.scatterplot(data=data, x='sepal_length', y='sepal_width', hue='variety', palette='Set1')
    plt.title(title)
    plt.show()

# Normalizacja Min-Max
def min_max_scaling(df):
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[['sepal_length', 'sepal_width']] = scaler.fit_transform(df[['sepal_length', 'sepal_width']])
    return df_scaled

# Skalowanie Z-score
def z_score_scaling(df):
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[['sepal_length', 'sepal_width']] = scaler.fit_transform(df[['sepal_length', 'sepal_width']])
    return df_scaled

# Tworzenie wykresów dla oryginalnych danych, Min-Max oraz Z-score
plot_iris(df, "Oryginalne dane")
df_min_max = min_max_scaling(df)
plot_iris(df_min_max, "Znormalizowane Min-Max")
df_z_score = z_score_scaling(df)
plot_iris(df_z_score, "Zeskalowane Z-score")

# Obliczenie statystyk dla danych oryginalnych
print("Statystyki dla oryginalnych danych:")
print(df[['sepal_length', 'sepal_width']].describe())

# Statystyki dla Min-Max
print("\nStatystyki dla danych znormalizowanych Min-Max:")
print(df_min_max[['sepal_length', 'sepal_width']].describe())

# Statystyki dla Z-score
print("\nStatystyki dla danych zeskalowanych Z-score:")
print(df_z_score[['sepal_length', 'sepal_width']].describe())
