# Write a Python program that displays all the even numbers from 1 to 20.

def DisplayEven():
    for number in range(1, 21):
        if number % 2 == 0:
            print(number, end=" ")
            
def main():
    DisplayEven()
    
if __name__ == "__main__":
    main()