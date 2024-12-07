import cv2
import numpy as np
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append((filename, img))
    return images

def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def preprocess_image(image):
    # Rozmycie obrazu, aby usunąć szum
    # blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Rozmycie medianowe
    median_blurred_image = cv2.medianBlur(image, 5)
    
    # # Filtr bilateralny
    bilateral_filtered_image = cv2.bilateralFilter(median_blurred_image, 9, 75, 75)

    return bilateral_filtered_image

def enhance_contrast(image):
    # Zwiększenie kontrastu i jasności
    # alpha = 1.4  # Współczynnik kontrastu
    # beta = 35    # Współczynnik jasności
    # enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # DZIAŁA CHUJOWO
    # Histogram Equalization 
    # equalized_image = cv2.equalizeHist(image)
    
    # # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(image)

    return clahe_image

def apply_threshold(image):
    # Zastosowanie progowania Otsu
    # _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    return binary_image

def count_birds(binary_image):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)

def main():
    folder_path = './bird_miniatures'
    images = load_images_from_folder(folder_path)

    for filename, image in images:
        scale_factor = 2
        width = int(image.shape[1] * scale_factor)
        height = int(image.shape[0] * scale_factor)
        enlarged_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)

        gray_image = convert_to_gray(enlarged_image)
        enhanced_image = enhance_contrast(gray_image)
        preprocessed_image = preprocess_image(enhanced_image)
        binary_image = apply_threshold(preprocessed_image)
        bird_count = count_birds(binary_image)
        print(f"{filename}: {bird_count} birds")

        # Wyświetlenie obrazów dla debugowania
        cv2.imshow("Original", enhanced_image)
        # cv2.imshow("Gray", gray_image)
        # cv2.imshow("Preprocessed", preprocessed_image)
        cv2.imshow("Binary", binary_image)
        # cv2.imshow("Morphed", morphed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()