# Program to find largest among three numbers using lambda function

LargestNumber = lambda a, b, c : a if (a > b and a > c) else (b if b > c else c)

def main():
    print("Enter three numbers :")
    no1 = int(input())
    no2 = int(input())
    no3 = int(input())
    
    ret = LargestNumber(no1, no2, no3)
    
    print("Largest number among", no1, ",", no2, "and", no3, "is :", ret)
    
if __name__ == "__main__":
    main()