# Program to check whether the given number is odd or not using lambda function

ChkOdd = lambda no : True if no % 2 != 0 else False

def main():
    print("Enter the number :")
    number = int(input())
    
    ret = ChkOdd(number)
    
    print(ret)
     
if __name__ == "__main__":
    main()