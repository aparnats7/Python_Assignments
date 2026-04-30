import numpy as np

def main():

    matrix = np.array([
        [6, 4],
        [8, 6]
    ])

    print("Input Matrix:")
    print(matrix)

    flattened = matrix.flatten()
    print("Flattened Output:")
    print(flattened)

    weights = np.array([0.5, 0.2, 0.1, 0.7])
    bias = 1

    print("Weights:", weights)
    print("Bias:", bias)

    print("\n--- Manual Calculation ---")

    result = 0
    for i in range(len(flattened)):
        mul = flattened[i] * weights[i]
        print(f"{flattened[i]} × {weights[i]} = {mul}")
        result += mul

    result += bias
    print(f"+ Bias ({bias})")

    print("Final Output =", result)

if __name__ == "__main__":
    main()