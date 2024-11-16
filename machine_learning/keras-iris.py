import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import tensorflow as tf

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Preprocess the data
# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encode the labels
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y.reshape(-1, 1))

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=42)

# # Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(y_encoded.shape[1], activation='softmax')
])

# # Definicja modelu
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(64, input_dim=X_train.shape[1], activation='tanh'),
#     tf.keras.layers.Dense(64, activation='tanh'),
#     tf.keras.layers.Dense(y_encoded.shape[1], activation='softmax'),
# ])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=tf.keras.optimizers.SGD(learning_rate=0.01))

# # Train the model
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2)
# # bardzo ostre skoki
# history = model.fit(X_train, y_train, epochs=100, batch_size=4, validation_split=0.2)
# łagodnieje
# history = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.2)


# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")

# Plot the learning curve
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.tight_layout()
plt.show()

# Save the model
model.save('iris_model.h5')

# Plot and save the model architecture
tf.keras.utils.plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)


# Rozpatrz poniższe problemy i pytania. Odpowiedzi do nich możesz zapisać jako rozszerzone komentarze w pliku
# pythonowym. Wykonaj różne modyfikacje programu, żeby odpowiedzieć na pytania.

# Co robi StandardScaler? Jak transformowane są dane liczbowe?
# 
# StandardScaler służy do standaryzacji danych.
# Standaryzacja oznacza przekształcenie danych tak, aby miały średnią równą 0 i odchylenie standardowe równe 1.
# a następnie używa tych wartości do przekształcenia danych.
# -----------------------------------------------------------------------------------------------------------------------------------
# Czym jest OneHotEncoder (i kodowanie „one hot” ogólnie)? Jak etykiety klas są transformowane przez ten encoder?
#
# OneHotEncoder to narzędzie, które służy do kodowania kategorii jako wektor na macierzy.
# Na przykład, jeśli mamy trzy klasy: 0, 1 i 2, to po kodowaniu one hot będą one reprezentowane jako:
# 0 -> [1, 0, 0]
# 1 -> [0, 1, 0]
# 2 -> [0, 0, 1]
# -----------------------------------------------------------------------------------------------------------------------------------
# Model ma 4 warstwy: wejściową, dwie ukryte warstwy z 64 neuronami każda i warstwę wyjściową. 
# Ile neuronów ma warstwa wejściowa i co oznacza X_train.shape[1]? Ile neuronów ma warstwa wyjściowa i co oznacza y_encoded.shape[1]?
#
# Model ma 4 warstwy: wejściową, dwie ukryte warstwy z 64 neuronami każda i warstwę wyjściową.
# Warstwa wejściowa modelu ma tyle neuronów, ile cech (feature) w zbiorze danych.
# X_train.shape[1] oznacza liczbę cech w zbiorze treningowym X_train.
# Warstwa wyjściowa modelu ma tyle neuronów, ile jest klas do przewidzenia.
# y_encoded.shape[1] oznacza liczbę unikalnych klas w zakodowanym zbiorze etykiet y_encoded.
# -----------------------------------------------------------------------------------------------------------------------------------
# Czy funkcja aktywacji relu jest najlepsza do tego zadania? Spróbuj użyć innej funkcji i obejrzyj wyniki
#
# tanh
# validation accuracy - 1 
# train accuracy 0.95 
# loss - poniej 0.1
#
# relu 
# validation acc - 0.95
# train acc - 0.97
# validation loss - 0.3
# trainloss - 0.06
# -----------------------------------------------------------------------------------------------------------------------------------
# Model jest konfigurowany do treningu za pomocą polecenia compile. Tutaj wybieramy optymalizator (algorytm,
# który używa gradientu straty do aktualizacji wag), funkcję straty, metrykę do oceny modelu. Eksperymentuj ze
# zmianą tych parametrów na inne i uruchom program. Czy różne optymalizatory lub funkcje straty dają różne
# wyniki? Czy możemy dostosować szybkość uczenia się w optymalizatorze?
#
# SGD jest szybciej ale gorsze wyniki
# -----------------------------------------------------------------------------------------------------------------------------------
# W linii model.fit sieć neuronowa jest trenowana. Czy jest sposób, by zmodyfikować tę linię tak, aby rozmiar
# partii był równy 4 lub 8 lub 16? Jak wyglądają krzywe uczenia się dla różnych parametrów? Jak zmiana partii
# wpływa na kształt krzywych? Wypróbuj różne wartości i uruchom program.
# -----------------------------------------------------------------------------------------------------------------------------------
# Co możesz powiedzieć o wydajności sieci neuronowej na podstawie krzywych uczenia? W której epoce sieć
# osiągnęła najlepszą wydajność? Czy ta krzywa sugeruje dobrze dopasowany model, czy mamy do czynienia z
# niedouczeniem lub przeuczeniem?
#
# Na podstawie krzywych uczenia możemy ocenić wydajność sieci neuronowej. Jeśli krzywa strat treningowych i walidacyjnych
# zbiega się do niskiej wartości, a dokładność treningowa i walidacyjna są wysokie i zbliżone do siebie, możemy powiedzieć,
# że model jest dobrze dopasowany.
#
# Jeśli krzywa strat walidacyjnych zaczyna rosnąć podczas gdy krzywa strat treningowych nadal maleje, może to sugerować
# przeuczenie (overfitting). W takim przypadku model uczy się zbyt dobrze na danych treningowych, ale nie generalizuje dobrze
# na nowych danych.
#
# Jeśli zarówno krzywa strat treningowych, jak i walidacyjnych są wysokie, a dokładność jest niska, może to sugerować
# niedouczenie (underfitting). W takim przypadku model nie jest w stanie dobrze nauczyć się wzorców w danych treningowych.
# -----------------------------------------------------------------------------------------------------------------------------------
# Przejrzyj niżej wymieniony kod i wyjaśnij co się w nim dzieje.
# 
# ten kod ładuje ponownie dane - standaryzacja - kodowanie kategorii - podział danych na zbiory
# ładuje juz wytrenowny wcześniej model
# i kontynuuje trening na następnych 10 przejściach
# zapisuje model i ocenia