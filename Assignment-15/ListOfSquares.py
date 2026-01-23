# Write a lambda function using map() to compute the square of each number in a given list.
 
Squares = lambda no : no ** 2

def main():
    data = [1, 2, 3, 4, 5]
    print("Original Data :", data)
    
    mData = list(map(Squares, data))

    print("Squared Data :", mData)

if __name__ == "__main__":
    main()