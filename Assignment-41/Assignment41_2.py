import math

# Function to calculate Euclidean Distance
def EucDistance(P1, P2):
    return math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)

def Predict(sorted_data, K):

    # If K is larger than dataset, take full dataset
    K = min(K, len(sorted_data))

    nearest = sorted_data[:K]

    votes = {}

    for n in nearest:
        label = n['label']
        votes[label] = votes.get(label, 0) + 1

    predicted_class = max(votes, key=votes.get)

    return predicted_class


def MarvellousKNN():

    border = "-" * 50

    data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 5, 'Y': 6, 'label': 'Blue'}
    ]

    print(border)
    print("KNN Prediction with Different K Values")
    print(border)

    x = int(input("Enter X coordinate: "))
    y = int(input("Enter Y coordinate: "))

    new_point = {'X': x, 'Y': y}

    # Calculate distances
    for d in data:
        d['distance'] = EucDistance(d, new_point)

    # Sort distances
    sorted_data = sorted(data, key=lambda item: item['distance'])

    print(border)
    print("Prediction Results")
    print(border)

    # Test different K values
    for K in [1, 3, 5]:
        result = Predict(sorted_data, K)
        print(f"K = {K} -> {result}")

    print(border)


def main():
    MarvellousKNN()


if __name__ == "__main__":
    main()