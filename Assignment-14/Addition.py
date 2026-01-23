# Program to perform addition of two numbers using lambda function

Addition = lambda a, b : a + b

def main():
    print("Enter the first number :")
    no1 = int(input())
    
    print("Enter the second number :")
    no2 = int(input())
    
    ret = Addition(no1, no2)
    
    print("Addition is :", ret)
    
if __name__ == "__main__":
    main()