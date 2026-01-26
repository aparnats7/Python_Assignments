# Write a Python function that takes two numbers as input and returns their sum.

def Add(a, b):
    return a + b

def main():
    print("Enter two numbers: ")
    num1 = int(input())
    num2 = int(input())
    
    result = Add(num1, num2)
    
    print(result)
    
if __name__ == "__main__":
    main()