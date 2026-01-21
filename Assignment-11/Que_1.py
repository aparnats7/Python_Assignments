# Program to check whether the given number is prime or not

def ChkPrime(no):
    for i in range(2, no):
        if no % i == 0:
            return False
        
    return True

def main():
    print("Enter number :")
    value = int(input())
    
    ret = ChkPrime(value)
    
    if ret == True:
        print("Prime Number")
        
    else:
        print("Not a Prime Number")
    
if __name__ == "__main__":
    main()