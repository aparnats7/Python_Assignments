# Write a lambda function using filter() to extract even numbers from a given list.

ChkEven = lambda x : (x % 2 == 0)

def main():
    data = [45, 63, 4, 18, 17, 72, 22, 9, 44]
    print("Original Data :", data)

    fData = list(filter(ChkEven, data))

    print("Even Numbers :", fData)

if __name__ == "__main__":
    main()