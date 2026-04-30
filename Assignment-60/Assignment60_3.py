# Loss Function Calculation

import numpy as np

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def binary_cross_entropy(y_true, y_pred):
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def main():
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([0.9, 0.2, 0.8, 0.7])

    print("MSE:", mse(y_true, y_pred))
    print("Binary Cross Entropy:", binary_cross_entropy(y_true, y_pred))

if __name__ == "__main__":
    main()