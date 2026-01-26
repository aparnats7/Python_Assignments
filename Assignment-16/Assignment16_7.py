# Write a Python function that checks whether a number is divisible by 5 or not.

def DivisibleBy5(No):
    if No % 5 == 0:
        return True
    
    else:
        return False
    
def main():
    print("Enter a number: ")
    Value = int(input())
    
    ret = DivisibleBy5(Value)
    
    print(ret)
    
if __name__ == "__main__":
    main()