# Write a program which accepts one number and return its square.

def Square(no):
    return no * no

def main():
    print("Enter number :")
    value = int(input())
    
    ret = Square(value)
    
    print("Square of number is :", ret)
    
if __name__ == "__main__":
    main()