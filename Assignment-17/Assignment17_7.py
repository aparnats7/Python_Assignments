# Write a program which accept number from user and display below pattern.

def Pattern(no):
    for i in range(1, no + 1):
        for j in range(1, no + 1):
            print(j, end=" ")

        print()
        
def main():
    print("Enter number :")
    Value = int(input())
    
    Pattern(Value)
    
if __name__ == "__main__":
    main()