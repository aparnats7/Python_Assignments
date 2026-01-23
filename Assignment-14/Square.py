# Program to find the square of a number using lambda function

Square = lambda no : no * no

def main():
    print("Enter a number :")
    value = int(input())
    
    result = Square(value)
    
    print("Square of", value, "is :", result)
    
    
if __name__ == "__main__":
    main()