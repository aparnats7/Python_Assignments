# Write a lambda function using reduce() to calculate the product of all elements in a given list.

from functools import reduce

Product = lambda x, y : x * y
def main():
    data = [10, 20, 30, 40, 50]
    
    rData = reduce(Product, data)
    
    print("Product of all elements :", rData)
    
if __name__ == "__main__":
    main()