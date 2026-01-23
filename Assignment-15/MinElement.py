# Write a lambda function using reduce() to find the minimum element in a given list.

from functools import reduce

MinElement = lambda a, b: a if (a < b) else b
def main():
    data = [10, 58, 23, 41, 67, 89, 12, 5]
    
    rData = reduce(MinElement, data)
    
    print("Minimum element in the list is :", rData)
    
if __name__ == "__main__":
    main()