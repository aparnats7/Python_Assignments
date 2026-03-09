import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def CheckAccuracy(X,Y):

    border = "-" * 50

    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    # Divide dataset into two equal parts
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    accuracy_scores = []
    k_values = range(1, len(X_train)+1)

    for k in k_values:

        model = KNeighborsClassifier(n_neighbors = k)

        model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test,Y_pred)

        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy report of all K values :")

    for k,value in zip(k_values,accuracy_scores):
        print("K =",k," Accuracy =",value*100)

    print(border)

    best_k = accuracy_scores.index(max(accuracy_scores)) + 1
    print("Best value of K is :",best_k)
    
def MarvellousClassifier(DataPath):
    
    border = "-" * 50
    
    # Step 1: Load the dataset
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)
    
    df = pd.read_csv(DataPath)

    print("First 5 records of dataset")
    print(df.head())
    
    print(border)

    # Step 2 : Clean and Prepare Data
    print(border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(border)

    df.dropna(inplace=True)

    print("Total records :",df.shape[0])
    print("Total columns :",df.shape[1])

    # Convert string data to numeric using LabelEncoder
    whetherEncoder = LabelEncoder()
    TempEncoder = LabelEncoder()
    ClassEncoder = LabelEncoder()

    df['Whether'] = whetherEncoder.fit_transform(df['Whether'])
    df['Temperature'] = TempEncoder.fit_transform(df['Temperature'])
    df['Play'] = ClassEncoder.fit_transform(df['Play'])

    print("Data after encoding")
    print(df.head())

    print(border)

    # Step 3 : Train Data using KNN
    print(border)
    print("Step 3 : Train Data using KNN Algorithm")
    print(border)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(X,Y)

    print("Training completed successfully")

    print(border)

    # Step 4 : Test Data
    print(border)
    print("Step 4 : Testing the trained model")
    print(border)

    Whether = int(input("Enter Whether value : "))
    Temperature = int(input("Enter Temperature value : "))

    test_data = pd.DataFrame([[Whether,Temperature]], columns=['Whether','Temperature'])

    result = model.predict(test_data)

    if(result[0] == 1):
        print("Play : Yes")
    else:
        print("Play : No")

    print(border)

    # Step 5 : Calculate Accuracy
    CheckAccuracy(X,Y)


def main():

    border = "-" * 50

    print(border)
    print("Play Predictor using KNN")
    print(border)

    MarvellousClassifier("PlayPredictor.csv")


if __name__ == "__main__":
    main()