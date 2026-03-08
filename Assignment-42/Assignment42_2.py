import math

def MarvellousSimpleLinearRegression():
    
    border = "-" * 50
    
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    
    print(border)
    print("Marvellous User Defined Simple Linear Regression")
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
    
    # Predict all Y values
    Y_pred = []
    
    print("Predicted Y values")
    print(border)
    
    for i in range(len(X)):
        y_hat = (m * X[i]) + c
        Y_pred.append(y_hat)
        print("X :",X[i],"Actual Y :",Y[i],"Predicted Y :",round(y_hat,2))
    
    print(border)
    
    # Calculate MSE
    mse_sum = 0
    
    print("Error Calculations")
    print(border)
    
    for i in range(len(Y)):
        error = Y[i] - Y_pred[i]
        sq_error = error ** 2
        mse_sum += sq_error
        
        print("Actual:",Y[i],
              "Predicted:",round(Y_pred[i],2),
              "Error:",round(error,2),
              "Squared Error:",round(sq_error,2))
    
    MSE = mse_sum / len(Y)
    
    print(border)
    print("Mean Squared Error (MSE) =",round(MSE,3))
    
    print(border)
    
    # Calculate R2 Score
    ss_res = mse_sum
    
    ss_tot = 0
    
    for i in range(len(Y)):
        ss_tot += (Y[i] - mean_y) ** 2
    
    r2 = 1 - (ss_res / ss_tot)
    
    print("SS_res =",round(ss_res,3))
    print("SS_tot =",round(ss_tot,3))
    print("R2 Score =",round(r2,3))
    
    print(border)


def main():
    MarvellousSimpleLinearRegression()

if __name__ == "__main__":
    main()