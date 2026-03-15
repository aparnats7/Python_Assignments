from sklearn.metrics import classification_report

def MarvellousClassificationReport():

    border = "-" * 50

    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    print(border)
    print("Classification Report")
    print(border)

    report = classification_report(actual,predicted)

    print(report)

    print(border)

def main():
    MarvellousClassificationReport()

if __name__ == "__main__":
    main()