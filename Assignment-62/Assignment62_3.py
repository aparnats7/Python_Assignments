import numpy as np

def main():
    image = np.array([
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1]
    ])

    kernel = np.array([
        [-1,-1,-1],
        [0,0,0],
        [1,1,1]
    ])

    output = []

    print("Image: ")
    print(image)

    print("Kernel: ")
    print(kernel)

    for i in range(3):
        row = []
        for j in range(3):

            region = image[i:i+3, j:j+3]

            print(f"Region at position ({i},{j}):\n{region}")

            print("Element-wise Multiplication:")
            mul = region * kernel
            print(mul)

            result = np.sum(mul)
            print("Sum =", result)

            row.append(result)

        output.append(row)

    print("Feature Map : ")
    for i in output:
        print(i)

if __name__ == "__main__":
    main()