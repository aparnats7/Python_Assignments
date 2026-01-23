# Write a lambda function using reduce() to calculate the addition of all elements in a given list.

from functools import reduce

Add = lambda x, y : x + y

def main():
    data = [10, 20, 30, 40, 50]
    
    rData = reduce(Add, data)
    
    print("Addition of all elements :", rData)
    
if __name__ == "__main__":
    main()