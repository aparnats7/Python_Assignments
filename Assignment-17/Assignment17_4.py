# Write a program which accept number from user and return the addition of its factors.

def FactorsAddition(no):
    sum = 0
    
    for i in range(1, no):
        if(no % i == 0):
            sum = sum + i
            
    return sum

def main():
    print("Enter number :")
    Value = int(input())
    
    Result = FactorsAddition(Value)
    
    print(Result)
    
if __name__ == "__main__":
    main()