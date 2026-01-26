# Write a program which contains one function named as ArithmeticOperations whichaccepts two numbers from user and returns addition, subtraction, multiplication and division of that two numbers. Write modular code by dividing code into modules.

import ArithmeticModule

def ArithmeticOperations(no1, no2):
    Ans1 = ArithmeticModule.Add(no1, no2)
    
    Ans2 = ArithmeticModule.Sub(no1, no2)
    
    Ans3 = ArithmeticModule.Mult(no1, no2)
    
    Ans4 = ArithmeticModule.Div(no1, no2)
    
    return Ans1, Ans2, Ans3, Ans4

def main():
    print("Enter first number:")
    Value1 = int(input())
    
    print("Enter second number:")
    Value2 = int(input())
    
    Addition, Subtraction, Multiplication, Division = ArithmeticOperations(Value1, Value2)
    
    print("Addition is:", Addition)
    print("Subtraction is:", Subtraction)
    print("Multiplication is:", Multiplication)
    print("Division is:", Division)
    
if __name__ == "__main__":
    main()