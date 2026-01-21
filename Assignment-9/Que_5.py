# Write a program which accepts one number and check whether that number is divisible by 3 and 5.
def ChkDivisibility(no):
    if no % 3 == 0 and no % 5 == 0:
        return True
    
    else:
        return False
    
def main():
    print("Enetr number :")
    value = int(input())
    
    ret = ChkDivisibility(value)
    
    if ret == True:
        print("Divisible by 3 and 5")
        
    else:
        print("Not Divisible by 3 and 5")
    
if __name__ == "__main__":
    main()