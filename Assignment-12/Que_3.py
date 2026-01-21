# Write a program which accept two numbers and print its addition, subtraction, multiplication and division.

def Calculator(no1, no2):
    ans1 = no1 + no2
    
    ans2 = no1 - no2
    
    ans3 = no1 * no2
    
    ans4 = no1 / no2
    
    print("Addition is : ", ans1)
    print("Subtraction is : ", ans2)
    print("Multiplication is : ", ans3)
    print("Division is : ", ans4)   
     
def main():
    print("Enter first number :")
    num1 = int(input())
    
    print("Enter second number :")
    num2 = int(input())
    
    Calculator(num1, num2)
    
if __name__ == "__main__":
    main()