# Factors of a Number

def Factors(no):
    for i in range(1, no+1):
        if no % i == 0:
            print(i, end=" ")
            
def main():
    print("Enter number :")
    value = int(input())
    
    Factors(value)
    
if __name__ == "__main__":
    main()