# Write a Python function that displays numbers from 10 to 1 in descending order when called.

def Display():
    for i in range(10, 0, -1):
        print(i, end=" ")
        
def main():
    Display()
    
if __name__ == "__main__":
    main()