# Activation Functions Visualization

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def main():
    x = np.linspace(-10, 10, 200)

    plt.figure()
    plt.plot(x, sigmoid(x), label="Sigmoid")
    plt.plot(x, relu(x), label="ReLU")
    plt.plot(x, tanh(x), label="Tanh")

    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()