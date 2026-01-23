# Program to find minimum between two numbers using lambda function

MinNumber = lambda a, b : a if a < b else b

def main():
    print("Enter two numbers :")
    value1 = int(input())
    value2 = int(input())
    
    ret = MinNumber(value1, value2)
    
    print("Minimum number between", value1, "and", value2, "is :", ret)
    
    
if __name__ == "__main__":
    main()