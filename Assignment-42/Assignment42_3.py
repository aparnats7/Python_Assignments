import matplotlib.pyplot as plt

def MarvellousLinearRegression():

    border = "-" * 50

    Experience = [1,2,3,4,5]
    Salary = [20000,25000,30000,35000,40000]

    print(border)
    print("Marvellous User Defined Linear Regression")
    print(border)

    print("Training Data Set")
    print(border)

    for i in range(len(Experience)):
        print("Experience :",Experience[i],"Salary :",Salary[i])

    print(border)

    # Mean
    mean_x = sum(Experience) / len(Experience)
    mean_y = sum(Salary) / len(Salary)

    print("Mean Experience =",mean_x)
    print("Mean Salary =",mean_y)

    print(border)

    # Calculate slope (m)
    num = 0
    den = 0

    for i in range(len(Experience)):
        num += (Experience[i] - mean_x) * (Salary[i] - mean_y)
        den += (Experience[i] - mean_x) ** 2

    m = num / den

    # Intercept
    c = mean_y - (m * mean_x)

    print("Slope (m) =",m)
    print("Intercept (c) =",c)

    print(border)

    print("Regression Equation")
    print("Salary =",m,"* Experience +",c)

    print(border)

    # Prediction for 6 years
    x_new = 6
    predicted_salary = (m * x_new) + c

    print("Predicted Salary for 6 Years Experience : ₹",predicted_salary)

    print(border)

    # Predicted values for plotting
    predicted = []

    for x in Experience:
        predicted.append((m * x) + c)

    # Plot graph
    plt.scatter(Experience, Salary, color='blue', label="Actual Data")
    plt.plot(Experience, predicted, color='red', label="Regression Line")

    plt.title("Experience vs Salary")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.legend()

    plt.show()


def main():
    MarvellousLinearRegression()

if __name__ == "__main__":
    main()