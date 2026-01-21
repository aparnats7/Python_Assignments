# Write a program which accept number from user and print even numbers upto that number.
def EvenNumber(no):
    for i in range(1, no + 1):
        if (i % 2 == 0):
            print(i, end=" ")
            
def main():
    print("Enter number :")
    value = int(input())
    
    EvenNumber(value)
    
if __name__ == "__main__":
    main()