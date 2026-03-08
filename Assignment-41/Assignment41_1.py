import math

# Function to calculate Euclidean Distance
def EucDistance(P1, P2):
    return math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)

def MarvellousKNN():
    
    border = "-" * 50

    # Dataset
    data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 5, 'Y': 6, 'label': 'Blue'}
    ]

    print(border)
    print("User Defined KNN Classifier")
    print(border)

    print("Training Dataset")
    for d in data:
        print(d)

    print(border)

    # Step 1: Accept user input
    x = int(input("Enter X coordinate: "))
    y = int(input("Enter Y coordinate: "))

    new_point = {'X': x, 'Y': y}

    # Step 2: Calculate distances
    for d in data:
        d['distance'] = EucDistance(d, new_point)

    print(border)
    print("Calculated Distances")
    print(border)

    for d in data:
        print(f"{d['point']} - Distance: {round(d['distance'],2)}")

    # Step 3: Sort distances
    sorted_data = sorted(data, key=lambda item: item['distance'])

    # Step 4: Select K = 3 nearest neighbors
    k = 3
    nearest = sorted_data[:k]

    print(border)
    print("Nearest Neighbors")
    print(border)

    for n in nearest:
        print(f"{n['point']} - Distance: {round(n['distance'],2)}")

    # Step 5: Majority Voting
    votes = {}
    for n in nearest:
        label = n['label']
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1

    predicted_class = max(votes, key=votes.get)

    print(border)
    print("Predicted Class:", predicted_class)
    print(border)


def main():
    MarvellousKNN()

if __name__ == "__main__":
    main()