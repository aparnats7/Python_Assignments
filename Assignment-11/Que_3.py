# Write a program which accept number from user and return the sum of its digits.

def SumOfDigits(no):
    sum = 0
    
    while no > 0:
        digit = no % 10
        
        sum = sum + digit
        
        no = no // 10
        
    return sum

def main():
    print("Enter number :")
    value = int(input())
    
    ret = SumOfDigits(value)
    
    print(ret)
    
if __name__ == "__main__":
    main()