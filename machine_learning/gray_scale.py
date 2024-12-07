import cv2
import numpy as np

def convert_to_gray(image):
    # Konwersja obrazu na skalę szarości metodą średniej
    B, G, R = cv2.split(image)
    gray_avg = np.round((R + G + B) / 3).astype(np.uint8)

    # Konwersja obrazu na skalę szarości metodą ważoną
    gray_weighted = np.round(0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)

    return gray_avg, gray_weighted

def display_images(original, gray_avg, gray_weighted):
    cv2.imshow("Original", original)
    cv2.imshow("Avg", gray_avg)
    cv2.imshow("ważone", gray_weighted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_paths = ['./images/elephant.jpg', './images/giraffe.jpg']

for path in image_paths:
    image = cv2.imread(path)
    if image is None:
        print(f"Nie można wczytać obrazu: {path}")
        continue

    gray_avg, gray_weighted = convert_to_gray(image)

    display_images(image, gray_avg, gray_weighted)