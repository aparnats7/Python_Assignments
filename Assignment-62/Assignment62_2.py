import numpy as np

def relu(x):
    return np.maximum(0, x)

def max_pooling(matrix):
    output = []

    for i in range(0, len(matrix), 2):
        row = []
        for j in range(0, len(matrix[0]), 2):

            block = matrix[i:i+2, j:j+2]

            print("Pooling Region:")
            print(block)

            max_val = np.max(block)
            print("Max Value:", max_val)

            row.append(max_val)

        output.append(row)

    return np.array(output)

def main():
    feature_map = np.array([
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ])

    print("Original Feature Map:")
    print(feature_map)

    relu_output = relu(feature_map)
    print("After ReLU (negative → 0):")
    print(relu_output)

    pooled_output = max_pooling(relu_output)

    print("Final Output after Max Pooling:")
    print(pooled_output)

if __name__ == "__main__":
    main()