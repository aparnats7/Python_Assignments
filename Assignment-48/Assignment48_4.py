import numpy as np
from sklearn.preprocessing import StandardScaler
import math

def MarvellousDistanceComparison():

    border = "-" * 50

    data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    print(border)
    print("Original Points")
    print(border)

    print(data)

    # Distance before scaling
    d1 = math.sqrt((data[0][0]-data[1][0])**2 + (data[0][1]-data[1][1])**2)

    print(border)
    print("Distance Before Scaling :",d1)

    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)

    print(border)
    print("Scaled Points")
    print(border)

    print(scaled)

    # Distance after scaling
    d2 = math.sqrt((scaled[0][0]-scaled[1][0])**2 + (scaled[0][1]-scaled[1][1])**2)

    print(border)
    print("Distance After Scaling :",d2)
    print(border)

def main():
    MarvellousDistanceComparison()

if __name__ == "__main__":
    main()