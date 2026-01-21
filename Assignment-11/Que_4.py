
def ReverseNumber(no):
    rev = 0
    
    while no > 0:
        digit = no % 10
        
        rev = (rev * 10) + digit
        
        no = no // 10
        
    return rev

def main():
    print("Enter number :")
    value = int(input())
    
    ret = ReverseNumber(value)
    
    print(ret)
    
if __name__ == "__main__":
    main()