# Write a program which accept number from user and display below pattern.

def Pattern(no):
    for i in range(no, 0, -1):
        for j in range(i):
            print("*", end="\t")
        print()
        
def main():
    print("Enter number :")
    Value = int(input())
    
    Pattern(Value)
    
if __name__ == "__main__":
    main()