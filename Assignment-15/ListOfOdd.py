# Write a lambda function using filter() to extract odd numbers from a given list.

ChkOdd = lambda x : (x % 2 != 0)

def main():
    data = [45, 63, 4, 18, 17, 72, 22, 9, 44]
    print("Original Data :", data)

    fData = list(filter(ChkOdd, data))

    print("Odd Numbers :", fData)

if __name__ == "__main__":
    main()