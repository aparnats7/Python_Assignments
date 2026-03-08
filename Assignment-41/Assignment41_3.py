import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['Hours'] - P2['Hours']) ** 2 + (P1['Attendance'] - P2['Attendance']) ** 2)
    return Ans

def MarvellousKNeighborsClassifier():
    border = "-" * 50
    
    data = [
                {'point': 'A', 'Hours': 2, 'Attendance': 60, 'label': 'Fail'},
                {'point': 'B', 'Hours': 5, 'Attendance': 80, 'label': 'Pass'},
                {'point': 'C', 'Hours': 6, 'Attendance': 85, 'label': 'Pass'},
                {'point': 'D', 'Hours': 1, 'Attendance': 50, 'label': 'Fail'}
            ]
    
    print(border)
    print("Marvellous User Defined KNN Classifier")
    print(border)
    
    print(border)
    print("Training Data Set")
    print(border)
    
    for i in data:
        print(i)
        
    print(border)
    
    # Accept user input
    h = int(input("Enter Study Hours : "))
    a = int(input("Enter Attendance : "))
    
    new_point = {'Hours': h, 'Attendance': a}
    
    # Calculate all distances
    for d in data:
        d['distance'] = EucDistance(d, new_point)
        
    print(border)
    print("Calculated Distances are : ")
    print(border)
    
    for d in data:
        print(d)
    
    sorted_data = sorted(data, key=lambda item: item['distance'])
    
    print(border)
    print("Sorted Data is : ")
    print(border)
    
    for d in sorted_data:
        print(d)
    
    k = 3
    nearest = sorted_data[:k]
    
    print(border)
    print("Nearest 3 elements are : ")  
    print(border)
    
    for d in nearest:
        print(d)
        
    # Voting
    votes = {}
    for neighbor in nearest:
        label = neighbor['label']
        votes[label] = votes.get(label, 0) + 1
        
    print(border)
    print("Voting Result is : ")
    print(border)
    
    for d in votes:
        print("Name : ", d, "Number of Votes : ", votes[d])
        
    print(border)
    
    predicted_class = max(votes, key=votes.get)
    
    print("Predicted Result : ", predicted_class)
    
def main():
    MarvellousKNeighborsClassifier()
    
if __name__ == "__main__":
    main()