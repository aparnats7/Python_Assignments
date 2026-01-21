# Write a program which accepts a number from user and convert it into binary format.

def ConvertBinary(no):
    binaryNum = bin(no)
    
    return binaryNum

def main():
    print("Enter number :")
    value = int(input())
    
    ret = ConvertBinary(value)
    
    print("It's binary equivalent is : ",ret)
    
if __name__ == "__main__":
    main()