# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers and performs the following operations:

import functools

FilterData = lambda no : no % 2 == 0

MapData = lambda no : no ** 2

ReduceData = lambda a, b : a + b

def main():
    lst = []
    print("Enter number of elements : ")
    n = int(input())
    
    print("Enter the elements : ")
    
    for i in range(n):
        value = int(input())
        lst.append(value)
        
    fData = list(filter(FilterData, lst))
    print("List after filter : ",fData)
    
    mData = list(map(MapData, fData))
    print("List after map : ",mData)
    
    rData = functools.reduce(ReduceData, mData)
    print("Output of reduce : ",rData)
    
if __name__ == "__main__":
    main()