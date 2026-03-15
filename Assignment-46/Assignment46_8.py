import numpy as np
from sklearn.linear_model import LinearRegression

def MarvellousLinearRegression():

    border = "-" * 50

    X = np.array([1,2,3,4,5]).reshape(-1,1)
    Y = np.array([50,55,60,65,70])

    model = LinearRegression()
    model.fit(X,Y)

    print(border)
    print("Prediction using Linear Regression")
    print(border)

    hours = np.array([[6]])

    predicted_marks = model.predict(hours)

    print("Predicted Marks for 6 Study Hours :",predicted_marks[0])

    print(border)

def main():
    MarvellousLinearRegression()

if __name__ == "__main__":
    main()