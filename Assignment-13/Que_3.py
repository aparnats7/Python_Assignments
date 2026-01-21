# Perfect Number

def ChkPerfect(no):
    sum = 0
    
    for i in range(1, no):
        if no % i == 0:
            sum = sum + i
            
    return sum

def main():
    print("Enter number :")
    value = int(input())
    
    ret = ChkPerfect(value)
   
    if ret == value:
        print("Perfect Number")
        
    else:
        print("Not a perfect number")
    
if __name__ == "__main__":
    main()