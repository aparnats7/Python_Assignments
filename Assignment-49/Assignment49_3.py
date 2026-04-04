import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from  sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report

def main():

    #-------------------------------------------------------------------------------
    # Step 1 :- EDA
    #-------------------------------------------------------------------------------

    Border = "-"*40

    print(Border)
    print("Step 1 :- EDA")
    print(Border)

    df = pd.read_csv("diabetes.csv")

    print("The shape of the dataset is: ",df.shape)

    print("The first 5 rows are: ")
    print(df.head())

    print("The column names: ")
    cols = df.columns.to_list()
    print(cols)

    print("The missing values are: ")
    print(df.isnull().sum())

    print("The basic statistical information is below: ",df.describe())

    sns.countplot(x = "Outcome", data = df)
    plt.title("Distribution of Diabetes Outcome")
    plt.show()

    print("The BoxPlot is below to identify the outliers")

    df.boxplot(figsize=(8,10))
    plt.show()

    #-------------------------------------------------------------------------------
    # Step 2 :- Data Preprocessing
    #-------------------------------------------------------------------------------

    print(Border)
    print("Step 2 :- Data Preprocessing")
    print(Border)

    cols_to_fix = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

    for col in cols_to_fix:
        df[col] = df[col].replace(0, df[col].mean())

    X = df.drop("Outcome", axis=1)
    Y = df["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    #-------------------------------------------------------------------------------
    # Step 3 :- Split the data
    #-------------------------------------------------------------------------------

    print(Border)
    print("Step 3 :-Split the data")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

    print("The shape of X_train: ",X_train.shape)
    print("The shape of X_test: ",X_test.shape)
    print("The shape of Y_train: ",Y_train.shape)
    print("The shape of Y_test: ",Y_test.shape)

    #-------------------------------------------------------------------------------
    # Step 4 :- Model Building
    #-------------------------------------------------------------------------------

    print(Border)
    print("Step 4 :- Model Building")
    print(Border)

    lr = LogisticRegression()
    lr.fit(X_train, Y_train)
    Y_pred_lr = lr.predict(X_test)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, Y_train)
    Y_pred_knn = knn.predict(X_test)

if __name__ == "__main__":
    main()