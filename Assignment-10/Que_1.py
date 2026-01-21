# Program to print multiplication table of a given number

def MultiTable(no):
    for i in range(1, 11):
        result = no * i
        
        print(result, end=" ")
        
def main():
    print("Enter number:")
    value = int(input())
    
    MultiTable(value)
    
if __name__ == "__main__":
    main()