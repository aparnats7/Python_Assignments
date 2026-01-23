# Write a lambda function using reduce() to find the maximum element in a given list.

from functools import reduce

MaxElement = lambda a, b: a if (a > b) else b

def main():
    data = [10, 58, 23, 41, 67, 89, 12, 5]
    
    rData = reduce(MaxElement, data)
    
    print("Maximum element in the list is :", rData)
    
if __name__ == "__main__":
    main()