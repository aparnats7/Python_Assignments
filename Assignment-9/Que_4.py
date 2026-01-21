# Write a program which accepts one number and return its cube.
def Cube(no):
    return no ** 3

def main():
    print("Enter number :")
    value = int(input())
    
    ret = Cube(value)
    
    print("The cube of number is : ",ret)
    
if __name__ == "__main__":
    main()