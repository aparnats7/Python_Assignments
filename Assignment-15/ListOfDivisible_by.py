# Write a lambda function using filter() to extract numbers divisible by both 3 and 5 from a given list.

ChkDivBy3and5 = lambda x : (x % 5 == 0) and (x % 3 == 0)
def main():
    data = [300, 58, 45, 41, 67, 89, 12, 15, 30]
    print("Original Data :", data)
    
    fData = list(filter(ChkDivBy3and5, data))
    print("Filtered Data :", fData)
    
if __name__ == "__main__":
    main()