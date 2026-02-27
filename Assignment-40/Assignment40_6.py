import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


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
        "SleepHours",
    ]

    X = df[feature_calls]
    Y = df["FinalResult"]

    print(" X shape : ",X.shape)
    print(" Y shape : ",Y.shape)

    # Scatter plot
    plt.figure(figsize=(7,5))

    for FR in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == FR]
        plt.scatter(temp["StudyHours"], temp["Attendance"], label=FR)

    plt.title("Student_performance_ml")
    plt.xlabel("StudyHours")
    plt.ylabel("Attendance")

    plt.legend()
    plt.grid(True)
    plt.show()

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Data splitting activity done : ")

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model.fit(X_train,Y_train)
    print("Model training completed")

    Y_pred = model.predict(X_test)

    print("Expected answers : ")
    print(Y_test.values)

    print("Predicted answers : ")
    print(Y_pred)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is: ",accuracy*100)

    misclassified_mask = (Y_test != Y_pred)
    misclassified_count = sum(misclassified_mask)

    print("\nTotal Misclassified Students:", misclassified_count)

    misclassified_students = X_test[misclassified_mask]

    print("\nMisclassified Student Records:")
    print(misclassified_students)

    print("\nActual Values:")
    print(Y_test[misclassified_mask].values)

    print("\nPredicted Values:")
    print(Y_pred[misclassified_mask])

if __name__ == "__main__":
    main()