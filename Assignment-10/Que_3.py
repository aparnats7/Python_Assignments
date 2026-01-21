# Program to find factorial of number 

def Factorial(no):
    if no < 0:
        return -1
    
    fact = 1
    
    for i in range(1, no+1):
        fact = fact * i
        
    return fact

def main():
    print("Enter number:")
    value = int(input())
    
    ret = Factorial(value)
    
    print(ret)
    
if __name__ == "__main__":
    main()