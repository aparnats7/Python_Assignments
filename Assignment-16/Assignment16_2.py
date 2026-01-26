# Write a Python function that checks whether a number is even or odd.

def ChkNum(no) :
    if(no % 2 == 0) :
        return True
    else :
        return False

def main():
    print("Enter a number: ")
    num = int(input())
    
    ret = ChkNum(num)
    
    if(ret == True):
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()