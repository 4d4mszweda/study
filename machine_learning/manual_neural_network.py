import math

def main() -> None:
    print(forward_pass(23,75,176))
    return

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def forward_pass(wiek: int, waga: int, wzrost: int) -> int:
    w1, w2, w3 = -0.46122, 0.97314, -0.39203
    w4, w5, w6 = 0.78548, 2.10584, -0.57847
    b1, b2 = 0.80109, 0.43529
    w_output1, w_output2 = -0.81546, 1.03775
    b_output = -0.2368

    hidden1 = wiek * w1 + waga * w2 + wzrost * w3 + b1
    hidden1_po_aktywacji = sigmoid(hidden1)
    hidden2 = wiek * w4 + waga * w5 + wzrost * w6 + b2
    hidden2_po_aktywacji = sigmoid(hidden2)
    output = hidden1_po_aktywacji * w_output1 + hidden2_po_aktywacji * w_output2 + b_output
    return output

if __name__ == "__main__":
    main()