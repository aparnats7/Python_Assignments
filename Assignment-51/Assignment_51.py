import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def main():

    # -----------------------------
    # STEP 1: LOAD DATA
    # -----------------------------
    fake = pd.read_csv("Fake.csv")
    true = pd.read_csv("True.csv")

    # Add labels
    fake["label"] = 0
    true["label"] = 1

    # Combine datasets
    data = pd.concat([fake, true], axis=0)

    print("The shape of dataset is: ",data.shape)

    print("The first 5 rows are: ")
    print(data.head())

    print("Column names are: ")
    print(data.columns.to_list())

    print("Missing values are: ")
    print(data.isnull().sum())

    # -----------------------------
    # STEP 2: PREPROCESSING
    # -----------------------------
    # Remove null values
    data = data.dropna()

    # Combine title + text
    data["content"] = data["title"] + " " + data["text"]

    # Features and Labels
    X = data["content"]
    Y = data["label"]

    # -----------------------------
    # STEP 3: TRAIN TEST SPLIT
    # -----------------------------
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("The shape of X_train: ",X_train.shape)
    print("The shape of X_test: ",X_test.shape)
    print("The shape of Y_train: ",Y_train.shape)
    print("The shape of Y_test: ",X_test.shape)

    # -----------------------------
    # STEP 4: TF-IDF
    # -----------------------------
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # -----------------------------
    # STEP 5: MODELS
    # -----------------------------
    lr = LogisticRegression()
    dt = DecisionTreeClassifier()

    # Train individual models
    lr.fit(X_train_vec, Y_train)
    dt.fit(X_train_vec, Y_train)

    # -----------------------------
    # STEP 6: VOTING CLASSIFIER
    # -----------------------------
    voting = VotingClassifier(
        estimators=[('lr', lr),
                    ('dt', dt)],
        voting='soft'   
    )

    voting.fit(X_train_vec, Y_train)

    # -----------------------------
    # STEP 7: PREDICTIONS
    # -----------------------------
    lr_pred = lr.predict(X_test_vec)
    dt_pred = dt.predict(X_test_vec)
    vote_pred = voting.predict(X_test_vec)

    # -----------------------------
    # STEP 8: EVALUATION
    # -----------------------------
    print("Logistic Regression Accuracy:", accuracy_score(Y_test, lr_pred)*100)
    print("Decision Tree Accuracy:", accuracy_score(Y_test, dt_pred)*100)
    print("Voting Classifier Accuracy:", accuracy_score(Y_test, vote_pred)*100)

    print("\nConfusion Matrix (Voting):")
    print(confusion_matrix(Y_test, vote_pred))

    print("\nClassification Report:")
    print(classification_report(Y_test, vote_pred))

if __name__ == "__main__":
    main()