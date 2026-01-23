# Program to find the cube of a number using lambda function

Cube = lambda x : x ** 3

def main():
    print("Enter a number :")
    value = int(input())
    result = Cube(value)
    print("Cube of", value, "is :", result)

if __name__ == "__main__":
    main()