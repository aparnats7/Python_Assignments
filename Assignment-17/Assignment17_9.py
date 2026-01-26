# Write a program which accept number from user and return the count of digits in that number.

def CountDigits(no):
    count = 0
    while no > 0:
        no = no // 10
        count += 1
    return count

def main():
    print("Enter number :")
    Value = int(input())
    
    Ret = CountDigits(Value)
    print(Ret)
    
if __name__ == "__main__":
    main()