# Program to check whether the given number is even or not using lambda function

ChkEven = lambda no : True if no % 2 == 0 else False

def main():
    print("Enter the number :")
    number = int(input())
    
    ret = ChkEven(number)
    
    print(ret)
     
if __name__ == "__main__":
    main()