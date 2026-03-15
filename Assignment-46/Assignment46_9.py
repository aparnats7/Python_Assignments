import numpy as np
from sklearn.linear_model import LinearRegression

def MarvellousMultipleLinearRegression():

    border = "-" * 50

    X = np.array([
        [1,7],
        [2,6],
        [3,7],
        [4,6],
        [5,8]
    ])

    Y = np.array([50,55,60,65,70])

    print(border)
    print("Marvellous Multiple Linear Regression")
    print(border)

    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficient for StudyHours :",model.coef_[0])
    print("Coefficient for SleepHours :",model.coef_[1])

    print("Intercept :",model.intercept_)

    print(border)

def main():
    MarvellousMultipleLinearRegression()

if __name__ == "__main__":
    main()