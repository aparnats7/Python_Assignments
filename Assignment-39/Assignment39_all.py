import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

Border = "-" * 50

#########################################################
# Step 1 : Dataset Loading
#########################################################

print(Border)
print("Step 1 : Dataset Loading")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

print("Dataset loaded successfully")
print("First 5 records:")
print(df.head())


#########################################################
# Step 2 : Data Analysis
#########################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape :", df.shape)
print("Column Names :", list(df.columns))
print("Class Distribution :")
print(df["FinalResult"].value_counts())


#########################################################
# Step 3 : Visualization
#########################################################

print(Border)
print("Step 3 : Visualization")
print(Border)

plt.figure()

passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]

plt.scatter(passed["StudyHours"], passed["PreviousScore"], 
            color="green", label="Pass")

plt.scatter(failed["StudyHours"], failed["PreviousScore"], 
            color="red", label="Fail")

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.show()


#########################################################
# Step 4 : Train-Test Split
#########################################################

print(Border)
print("Step 4 : Train-Test Split")
print(Border)

X = df[["StudyHours", "Attendance", "PreviousScore",
        "AssignmentsCompleted", "SleepHours"]]

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

print("Training shape :", X_train.shape)
print("Testing shape :", X_test.shape)


#########################################################
# Step 5 : Model Training
#########################################################

print(Border)
print("Step 5 : Model Training")
print(Border)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

print("Model trained successfully")


#########################################################
# Step 6 : Prediction
#########################################################

print(Border)
print("Step 6 : Prediction")
print(Border)

Y_pred = model.predict(X_test)

print("Actual Values :")
print(Y_test.values)

print("Predicted Values :")
print(Y_pred)


#########################################################
# Step 7 : Accuracy Calculation
#########################################################

print(Border)
print("Step 7 : Accuracy Calculation")
print(Border)

test_accuracy = accuracy_score(Y_test, Y_pred)
train_accuracy = accuracy_score(Y_train, model.predict(X_train))

print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))
print("Testing Accuracy  : {:.2f}%".format(test_accuracy * 100))


#########################################################
# Step 8 : Confusion Matrix Generation
#########################################################

print(Border)
print("Step 8 : Confusion Matrix Generation")
print(Border)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix :")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=["Fail", "Pass"])
disp.plot()
plt.title("Confusion Matrix")
plt.show()


#########################################################
# Step 9 : Final Conclusion
#########################################################

print(Border)
print("Step 9 : Final Conclusion")
print(Border)

if train_accuracy > test_accuracy:
    print("Model may be Overfitting.")
elif train_accuracy < test_accuracy:
    print("Model may be Underfitting.")
else:
    print("Model is Balanced.")

print("Decision Tree model successfully trained and evaluated.")