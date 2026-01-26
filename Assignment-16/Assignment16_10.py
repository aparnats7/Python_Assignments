# This program calculates the length of a given string without using built-in functions.

def NameLength(s):
    length = 0
    
    for char in s:
        length += 1
        
    return length

def main():
    print("Enter your name: ")
    name = input()
    
    length = NameLength(name)
    
    print(length)
    
if __name__ == "__main__":
    main()