# Write a program which contains one lambda function which accepts one parameter 
# and return its multiplication of two numbers.

Multiplication = lambda no1, no2 : no1 * no2

def main():
    print("Enter first number")
    value1 = int(input())
    
    print("Enter second number")
    value2 = int(input())

    ret = Multiplication(value1, value2)
    
    print(ret)
    
if __name__ == "__main__":
    main()