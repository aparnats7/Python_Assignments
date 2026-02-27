import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40

#########################################################
# Step 1 : Load the dataset
#########################################################
print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")

#########################################################
# Step 2 : Data Analysis (EDA)
#########################################################

print(Border)
print("Step 2 : Data analysis")
print(Border)

print("First 5 entries from dataset :")
print(df.head())

print("Last 5 entries from dataset :")
print(df.tail())

print("Total number of rows and columns in dataset : ")
print(df.shape)

print("List of column names in dataset : ")
print(df.columns.tolist())

print("Data types of each column in dataset : ")
print(df.dtypes)

total_students = len(df)
passed_students = len(df[df["FinalResult"] == 1])
failed_students = len(df[df["FinalResult"] == 0])

print("Total number of students:", total_students)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)

#########################################################
# Step 3 : Statistical Analysis 
#########################################################

print(Border)
print("Step 3 : Statistical analysis")
print(Border)

print("Average StudyHours :")
print(df["StudyHours"].mean())
print("Average Attendance :")
print(df["Attendance"].mean())
print("Maximum PreviousScore :")
print(df["PreviousScore"].max())
print("Minimum SleepHours :")
print(df["SleepHours"].min())

#########################################################
# Step 4 : FINAL RESULT DISTRIBUTION
#########################################################

print(Border)
print("Step 4 : Final Result Distribution")
print(Border)

result_counts = df["FinalResult"].value_counts()
print(result_counts)

percentage = df["FinalResult"].value_counts(normalize=True) * 100
print("Percentage Distribution:")
print(percentage)

#########################################################
# Step 5 : ANALYSIS OBSERVATIONS
#########################################################

print(Border)
print("Step 5 : Analysis Observations")
print(Border)

avg_pass_study = df[df["FinalResult"] == 1]["StudyHours"].mean()
avg_fail_study = df[df["FinalResult"] == 0]["StudyHours"].mean()

avg_pass_att = df[df["FinalResult"] == 1]["Attendance"].mean()
avg_fail_att = df[df["FinalResult"] == 0]["Attendance"].mean()

print("Average StudyHours (Pass):", avg_pass_study)
print("Average StudyHours (Fail):", avg_fail_study)

print("Average Attendance (Pass):", avg_pass_att)
print("Average Attendance (Fail):", avg_fail_att)

print("Observation:")
if avg_pass_study > avg_fail_study:
    print("- Students who passed studied more hours on average.")
else:
    print("- Study hours do not significantly affect passing.")

if avg_pass_att > avg_fail_att:
    print("- Higher attendance improves chances of passing.")
else:
    print("- Attendance does not significantly affect passing.")

#########################################################
# Step 6 : Histogram of StudyHours
#########################################################

print(Border)
print("Step 6 : Histogram of StudyHours")
print(Border)

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x="StudyHours", hue="FinalResult", multiple="stack")
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()
