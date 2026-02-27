
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score
)


def main():   
    DatasetPath = "Student_performance_ml.csv"

    df = pd.read_csv(DatasetPath)

    print("Dataset gets loaded successfully...")
    print("Initial entries from dataset :")
    print(df.head())

    print("Shape of dataset : ",df.shape)
    print("Column Names : ",list(df.columns))

    print("Missing Values (Per column): ")
    print(df.isnull().sum())

    print("Class Distribution (FinalResult count)")
    print(df["FinalResult"].value_counts())

    print("Statistial Report of Dataset")
    print(df.describe())

    feature_calls = [
        "StudyHours", 
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
        ]
    X = df[feature_calls]
    Y = df["FinalResult"]
    print(" X shape : ",X.shape)
    print(" Y shape : ",Y.shape)

    # Scatter plot
    plt.figure(figsize=(7,5))

    for FR in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == FR]
        plt.scatter(temp["StudyHours"], temp["Attendance"], label = FR)

    plt.title("Student_performance_ml")
    plt.xlabel("StudyHours")
    plt.ylabel("Attendance")

    plt.legend()
    plt.grid(True)
    plt.show()

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = 0.2,
        random_state = 42
    )

    print("Data splitting activity done : ")

    print("X - Independent : ",X.shape)   
    print("Y - Dependent: ",Y.shape)      

    print("X_train : ",X_train.shape)     
    print("X_test : ",X_test.shape)     

    print("Y_train : ",Y_train.shape)     
    print("Y_test: ",Y_test.shape)        

    print("We are going to use DecisionTreeClassifier")

    model = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42

    )

    print("Model successfully created : ",model)

    model.fit(X_train,Y_train)

    print("Model training completed")

    Y_pred = model.predict(X_test)

    print("Model evaluation (testing) complete")

    print(Y_pred.shape)

    print("Expected answers : ")
    print(Y_test)

    print("Predicted answers : ")
    print(Y_pred)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is: ",accuracy*100)

    new_students = pd.DataFrame({
        "StudyHours": [2, 6, 4, 8, 1],
        "Attendance": [60, 85, 75, 95, 50],
        "PreviousScore": [55, 80, 65, 90, 40],
        "AssignmentsCompleted": [3, 8, 5, 9, 2],
        "SleepHours": [6, 7, 5, 8, 4]
    })

    predictions = model.predict(new_students)

    new_students["PredictedResult"] = predictions

    print("Predictions for 5 New Students:")
    print(new_students)
    


if __name__ == "__main__":
    main()