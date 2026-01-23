# Write a lambda function using filter() and return the count of even numbers from a given list.

ChkEven = lambda x : (x % 2 == 0)

def main():
    data = [45, 63, 4, 18, 17, 72, 22, 9, 44]
    print("Original Data :", data)

    fData = list(filter(ChkEven, data))

    count = 0
    
    for i in fData:
        count += 1
    
    print("Count of Even Numbers :", count)

if __name__ == "__main__":
    main()