# # Write a program which accepts N numbers from user and store them into List. 
# # Return addition of all prime elements from that List.

import ChkPrime

def ListPrime(lst, no):
    plist = []
    for i in range(len(lst)):
        if ChkPrime.Prime(lst[i]):
            plist.append(lst[i])
    return plist

def Addition(a, b):
    return a + b

def main():
    lst = []

    n = int(input("Enter number of elements : "))
    print("Enter elements : ")

    for i in range(n):
        element = int(input())
        lst.append(element)

    plist = ListPrime(lst, n)

    total = 0
    for i in range(len(plist)):
        total = Addition(total, plist[i])

    print(total)

if __name__ == "__main__":
    main()
