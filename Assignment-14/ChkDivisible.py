# Program to check whether the given number is divisible by 5 or not using lambda function

ChkDivisibility = lambda no : True if no % 5 == 0 else False

def main():
    print("Enter the number :")
    number = int(input())
    
    ret = ChkDivisibility(number)
    
    print(ret)
     
if __name__ == "__main__":
    main()