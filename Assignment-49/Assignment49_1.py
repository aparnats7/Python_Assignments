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
    print(df.columns.to_list())

    print("The missing values are: ")
    print(df.isnull().sum())

    print("The basic statistical information is below: ",df.describe())

    sns.countplot(x = "Outcome", data = df)
    plt.title("Distribution of Diabetes Outcome")
    plt.show()

    print("The BoxPlot is below to identify the outliers")

    df.boxplot(figsize=(8,10))
    plt.show()

if __name__ == "__main__":
    main()