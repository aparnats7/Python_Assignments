# Write a program which contains one function named as ChkGreater.
# That function should accept two parameters and it should return greater
# number. If both parameters are equal then return -1.

def ChkGreater(no1, no2):
    if no1 > no2:
        return no1
    
    elif no2 > no1:
        return no2
    
    else:
        return -1
def main():
    num1 = print("Enter first number:")
    num1 = int(input())
    
    num2 = print("Enter second number:")
    num2 = int(input())
    
    ret = ChkGreater(num1, num2)
    
    print("Greater number is:", ret)
    
if __name__ == "__main__":
    main()