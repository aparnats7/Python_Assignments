# Write a program which contains one lambda function which accepts one parameter and return its power of 2.

Power = lambda no : 2 ** no

def main():
    print("Enter a number")
    value = int(input())

    ret = Power(value)
    
    print(ret)
    
if __name__ == "__main__":
    main()