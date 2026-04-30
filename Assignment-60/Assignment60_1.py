# Artificial Neuron Simulation

import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def neuron(inputs, weights, bias):
    z = np.dot(weights, inputs) + bias
    y = sigmoid(z)
    print("Weighted Sum:", z)
    print("Output:", y)

def main():
    inputs = [2, 3]
    weights = [0.4, 0.6]
    bias = 0.5
    neuron(inputs, weights, bias)

if __name__ == "__main__":
    main()