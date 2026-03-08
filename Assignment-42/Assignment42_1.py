import math

def MarvellousSimpleLinearRegression():
    
    border = "-" * 50
    
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    
    print(border)
    print("Marvellous User Defined Simple Linear Regression")
    print(border)
    
    print(border)
    print("Training Data Set")
    print(border)
    
    for i in range(len(X)):
        print("X :",X[i],"Y :",Y[i])
        
    print(border)
    
    # Mean of X
    mean_x = sum(X) / len(X)
    
    # Mean of Y
    mean_y = sum(Y) / len(Y)
    
    print("Mean of X =",mean_x)
    print("Mean of Y =",mean_y)
    
    print(border)
    
    # Calculate Slope (m)
    num = 0
    den = 0
    
    for i in range(len(X)):
        num = num + ((X[i] - mean_x) * (Y[i] - mean_y))
        den = den + ((X[i] - mean_x) ** 2)
        
    m = num / den
    
    # Intercept (c)
    c = mean_y - (m * mean_x)
    
    print("Slope (m) =",round(m,2))
    print("Intercept (c) =",round(c,2))
    
    print(border)
    
    print("Regression Equation :")
    print("Y =",round(m,2),"X +",round(c,2))
    
    print(border)
    
    # Prediction
    x_new = 6
    y_pred = (m * x_new) + c
    
    print("Predicted Y for X =",x_new,":",round(y_pred,2))
    
    print(border)

def main():
    MarvellousSimpleLinearRegression()

if __name__ == "__main__":
    main()