# Program to perform multiplication of two numbers using lambda function

Multiplication = lambda a, b : a * b

def main():
    print("Enter the first number :")
    no1 = int(input())
    
    print("Enter the second number :")
    no2 = int(input())
    
    ret = Multiplication(no1, no2)
    
    print("Multiplication is :", ret)
    
if __name__ == "__main__":
    main()