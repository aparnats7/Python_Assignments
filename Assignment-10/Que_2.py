# Write a program which accepts one number and prints sum of its natural numbers.

def DisplaySum(no1):
    sum = 0
    for i in range(no1+1):
        sum = sum + i
        
    return sum
    
def main():
    print("Enter natural number :")
    value = int(input())
    
    ret = DisplaySum(value)
    
    print(ret)
    
if __name__ == "__main__":
    main()