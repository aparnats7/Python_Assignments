import numpy as np
from sklearn.linear_model import LinearRegression

def MarvellousLinearRegression():

    border = "-" * 50

    X = np.array([1,2,3,4,5]).reshape(-1,1)
    Y = np.array([50,55,60,65,70])

    print(border)
    print("Marvellous Linear Regression Model")
    print(border)

    print(border)
    print("Training Data Set")
    print(border)

    for i in range(len(X)):
        print("Study Hours :",X[i][0],"Marks :",Y[i])

    print(border)

    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficient :",model.coef_[0])
    print("Intercept :",model.intercept_)

    print(border)

def main():
    MarvellousLinearRegression()

if __name__ == "__main__":
    main()