import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from tensorflow.keras.callbacks import History, ModelCheckpoint


# Load dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess data
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
original_test_labels = np.argmax(test_labels, axis=1)  # Save original labels for confusion matrix

# Define model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# CHECKPOINT
checkpoint = ModelCheckpoint('best_model.keras', monitor='val_accuracy', save_best_only=True, mode='max', verbose=1)

# Train model
history = History()
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2, callbacks=[history])

# Evaluate on test set
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.4f}")

# Predict on test images
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)

# Confusion matrix
cm = confusion_matrix(original_test_labels, predicted_labels)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Plotting training and validation accuracy
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

# Plotting training and validation loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.tight_layout()
plt.show()

# Display 25 images from the test set with their predicted labels
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(predicted_labels[i])
plt.show()


# a) Co się dzieje w preprocessing? Do czego służy funkcja reshape, to_categorical i np.argmax?

# W preprocessing danych przygotowujemy dane wejściowe do modelu. Obejmuje to normalizację, zmianę kształtu danych
# oraz kodowanie etykiet.

# Funkcja reshape:
# Funkcja reshape zmienia kształt danych. Na przykład, jeśli mamy dane obrazów w formacie 28x28 pikseli, możemy
# zmienić ich kształt na (28, 28, 1) dla modelu CNN, który oczekuje danych w formacie (wysokość, szerokość, liczba kanałów).

# Przykład:
# X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)

# Funkcja to_categorical:
# Funkcja to_categorical zamienia etykiety klas na format one-hot encoding. Każda etykieta jest reprezentowana jako
# wektor binarny z jedynką na pozycji odpowiadającej danej klasie i zerami na pozostałych pozycjach.

# Przykład:
# y_train = to_categorical(y_train, num_classes)

# Funkcja np.argmax:
# Funkcja np.argmax zwraca indeks maksymalnej wartości wzdłuż określonej osi. Jest często używana do zamiany
# wektorów one-hot encoding z powrotem na etykiety klas.

# Przykład:
# y_pred = np.argmax(model.predict(X_test), axis=1)



# b) Jak dane przepływają przez sieć i jak się w niej transformują? Co każda z warstw dostaje na wejście i co wyrzuca na wyjściu?

# W sieci CNN (Convolutional Neural Network) dane przepływają przez różne warstwy, które przekształcają je w różny sposób.
# Oto typowy przepływ danych przez sieć CNN:

# 1. Warstwa wejściowa:
# Dane wejściowe to obrazy o kształcie (28, 28, 1) dla obrazów MNIST. Każdy obraz jest reprezentowany jako macierz pikseli.

# 2. Warstwa konwolucyjna (Conv2D):
# Warstwa konwolucyjna stosuje filtry (kernels) do danych wejściowych, aby wyodrębnić cechy (features).
# Na przykład, Conv2D(32, kernel_size=(3, 3), activation='relu') stosuje 32 filtry 3x3 do danych wejściowych.
# Wyjście: macierz cech o kształcie (26, 26, 32) (zakładając brak paddingu).

# 3. Warstwa normalizacji (BatchNormalization):
# Normalizuje dane wyjściowe z poprzedniej warstwy, aby przyspieszyć trening i stabilizować sieć.
# Wyjście: macierz cech o tym samym kształcie co wejście.

# 4. Warstwa aktywacji (Activation):
# Stosuje funkcję aktywacji (np. ReLU) do danych wyjściowych z poprzedniej warstwy.
# Wyjście: macierz cech o tym samym kształcie co wejście.

# 5. Warstwa pooling (MaxPooling2D):
# Redukuje wymiary danych, wybierając maksymalne wartości w oknach (np. 2x2).
# Na przykład, MaxPooling2D(pool_size=(2, 2)) redukuje wymiary o połowę.
# Wyjście: macierz cech o kształcie (13, 13, 32).

# 6. Warstwa spłaszczająca (Flatten):
# Przekształca macierz cech w wektor jednowymiarowy.
# Wyjście: wektor o długości 13*13*32.

# 7. Warstwa w pełni połączona (Dense):
# Stosuje pełne połączenia do wektora cech, aby dokonać klasyfikacji.
# Na przykład, Dense(128, activation='relu') stosuje 128 neuronów do wektora cech.
# Wyjście: wektor o długości 128.

# 8. Warstwa wyjściowa (Dense):
# Stosuje pełne połączenia do wektora cech, aby dokonać ostatecznej klasyfikacji.
# Na przykład, Dense(10, activation='softmax') stosuje 10 neuronów (po jednym dla każdej klasy).
# Wyjście: wektor o długości 10, reprezentujący prawdopodobieństwa przynależności do każdej klasy.



# c) Jakich błędów na macierzy błędów jest najwięcej. Które cyfry są często mylone z jakimi innymi?

# najczęściej mylona jest 5 z 8

# d) Co możesz powiedzieć o krzywych uczenia się. Czy mamy przypadek przeuczenia lub niedouczenia się?

# lekkie nieduczenie

# e) Jak zmodyfikować kod programu, aby model sieci był zapisywany do pliku h5 co epokę, pod warunkiem, że w tej epoce osiągnęliśmy lepszy wynik?