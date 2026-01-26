# Write a program which accepts number from user and print that number of stars on screen.

def Display(no):
    for i in range(no):
        print("*", end=" ")
        
def main():
    print("Enter number of stars to print: ")
    Value = int(input())
    
    Display(Value)
    
if __name__ == "__main__":
    main()