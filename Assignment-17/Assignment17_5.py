# Write a program which checks whether 5 is prime number or not.

def ChkPrime(no):   
    count = 0
    
    for i in range(1, no + 1):
        if(no % i == 0):
            count = count + 1
            
    if(count == 2):
        return True
    
def main():
    print("Enter number :")
    Value = int(input())
    
    bRet = ChkPrime(Value)
    
    if(bRet == True):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")
        
if __name__ == "__main__":
    main() 