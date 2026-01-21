# Write a program which accept number from user and display its sequence from 1 to N.
def Sequence(no):
    for i in range(1, no+1):
        print(i, end=" ")
        
def main():
    print("Enter number :")
    value = int(input())
    
    Sequence(value)
    
if __name__ == "__main__":
    main()