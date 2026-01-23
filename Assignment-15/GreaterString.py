# Write a lambda function using filter() to extract strings with length greater than 5 from a given list.

GreaterStrings = lambda s: len(s) > 5

def main():
    data = ["Rohit", "Shubhman", "Abhishek", "Virat", "Suryakumar", "Hardik", "Tilak"]
    print("Original Data :", data)
    
    fData = list(filter(GreaterStrings, data))
    print("Filtered Data :", fData)

if __name__ == "__main__":
    main()