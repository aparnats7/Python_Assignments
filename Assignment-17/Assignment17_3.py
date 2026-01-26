# Write a program which accept number from user and return its factorial.

def Factorial(no):
    fact = 1
    
    for i in range(1, no + 1):
        fact = fact * i
        
    return fact

def main():
    print("Enter number :")
    Value = int(input())
    
    Result = Factorial(Value)
    
    print(Result)
    
if __name__ == "__main__":
    main()