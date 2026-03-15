import numpy as np

def CalculateVariance(arr):
    variance = np.var(arr)
    return variance

def CalculateStandardDeviation(arr):
    std_dev = np.std(arr)
    return std_dev

def main():
    data = np.array([6, 7, 8, 9, 10, 11, 12])
    
    variance_value = CalculateVariance(data)
    print("Variance of the dataset is : ", variance_value)
    
    std_dev_value = CalculateStandardDeviation(data)
    print("Standard Deviation of the dataset is : ", std_dev_value)

if __name__ == "__main__":
    main()