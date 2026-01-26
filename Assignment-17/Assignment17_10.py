# Write a program which accept number from user and return the addition of digits in that number.

def AddDigits(no):
    sum = 0
    while no > 0:
        digit = no % 10
        sum = sum + digit
        
        no = no // 10
        
    return sum

def main():
    print("Enter number :")
    Value = int(input())
    
    Ret = AddDigits(Value)
    print(Ret)
    
if __name__ == "__main__":
    main()