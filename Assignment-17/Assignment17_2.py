# Write a program which accept number from user and display below pattern.

def StarPattern(no):
    for i in range(no):
        for j in range(no):
            print("*", end=" ")
        print()
    
def main():
    print("Enter number :")
    Value = int(input())
    
    StarPattern(Value)
    
if __name__ == "__main__":
    main()