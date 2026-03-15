import numpy as np

def CalculateMean(arr):
    mean = np.mean(arr)
    return mean
def main():
    data = np.array([6, 7, 8, 9, 10, 11, 12])
    mean_value = CalculateMean(data)
    print("Mean of the dataset is : ", mean_value)

if __name__ == "__main__":
    main()