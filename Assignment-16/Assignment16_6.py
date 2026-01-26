# Write a Python function that checks whether a number is positive, negative, or zero.

def ChkNumber(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")
        
def main():
    print("Enter a number: ")
    Value = int(input())
    
    ChkNumber(Value)
    
if __name__ == "__main__":
    main() 