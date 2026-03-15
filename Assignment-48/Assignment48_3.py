import numpy as np
from sklearn.preprocessing import StandardScaler

def MarvellousFeatureScaling():

    border = "-" * 50

    data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    print(border)
    print("Original Dataset")
    print(border)

    print(data)

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)

    print(border)
    print("Scaled Dataset")
    print(border)

    print(scaled_data)

    print(border)

def main():
    MarvellousFeatureScaling()

if __name__ == "__main__":
    main()