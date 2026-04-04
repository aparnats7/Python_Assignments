import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve


def main():
    Border = "-" * 40

    #----------------------------------------------------
    # Step 1 :- load and explore the dataset
    #----------------------------------------------------

    print(Border)
    print("Step 1 :- load and explore the dataset")
    print(Border)

    df = pd.read_csv("bank-full.csv", sep=';')

    # Clean column names
    df.columns = df.columns.str.strip().str.replace('"', '').str.replace("'", "")

    print("Columns:", list(df.columns))
    print("Shape:", df.shape)
    print("First 5 records:\n", df.head())

    print("Missing Values:\n", df.isnull().sum())

    print("Dataset Info:")
    df.info()

    # Replace 'unknown'
    df.replace("unknown", np.nan, inplace=True)

    # Fill missing values using mode
    df.fillna(df.mode().iloc[0], inplace=True)

    # Detect target column safely
    target_col = [col for col in df.columns if col.strip().lower() == 'y'][0]

    print("Target column:", target_col)

    # Plot target distribution
    sns.countplot(x=target_col, data=df)
    plt.title("Target Distribution")
    plt.show()

    #----------------------------------------------------
    # Step 2 :- Data Preprocessing
    #----------------------------------------------------

    print(Border)
    print("Step 2 :- Data Preprocessing")
    print(Border)

    # Encode target
    df[target_col] = df[target_col].map({'yes': 1, 'no': 0})

    # Encode categorical columns
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    print("After Encoding:\n", df.head())

    # Split data
    X = df.drop(target_col, axis=1)
    Y = df[target_col]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    #----------------------------------------------------
    # Step 3 :- Train Test Split
    #----------------------------------------------------

    print(Border)
    print("Step 3 :- Train Test Split")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X_scaled, Y, test_size=0.2, random_state=42
    )

    #----------------------------------------------------
    # Step 4 :- Model Building
    #----------------------------------------------------

    print(Border)
    print("Step 4 :- Model Building")
    print(Border)

    lr = LogisticRegression(max_iter=1000)
    knn = KNeighborsClassifier()
    rf = RandomForestClassifier()

    lr.fit(X_train, Y_train)
    knn.fit(X_train, Y_train)
    rf.fit(X_train, Y_train)

    #----------------------------------------------------
    # Step 5 :- Model Evaluation
    #----------------------------------------------------

    print(Border)
    print("Step 5 :- Model Evaluation")
    print(Border)

    models = {
        "Logistic Regression": lr,
        "KNN": knn,
        "Random Forest": rf
    }

    for name, model in models.items():

        Y_pred = model.predict(X_test)

        print("\n", "="*20, name, "="*20)

        print("Accuracy:", accuracy_score(Y_test, Y_pred))
        print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
        print("Classification Report:\n", classification_report(Y_test, Y_pred))

        if hasattr(model, "predict_proba"):
            Y_prob = model.predict_proba(X_test)[:, 1]
            print("ROC-AUC Score:", roc_auc_score(Y_test, Y_prob))

    #----------------------------------------------------
    # Step 6 :- ROC Curve
    #----------------------------------------------------

    print(Border)
    print("Step 6 :- ROC Curve")
    print(Border)

    for name, model in models.items():
        if hasattr(model, "predict_proba"):
            Y_prob = model.predict_proba(X_test)[:, 1]
            fpr, tpr, _ = roc_curve(Y_test, Y_prob)
            plt.plot(fpr, tpr, label=name)

    plt.plot([0, 1], [0, 1], linestyle='--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()