# Write a program which accept number from user and display its reverse sequence.

def ReverseSequence(no):
    for i in range(no, 0, -1):
        print(i, end=" ")
        
def main():
    print("Enter number :")
    value = int(input())
    
    ReverseSequence(value)
    
if __name__ == "__main__":
    main()