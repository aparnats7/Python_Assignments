# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers and performs the following operations:

import functools

def FilterData(no):
    count = 0
    for i in range(1, no + 1):
        if(no % i == 0):
            count = count + 1
            
    if(count == 2):
        return True
    
def MapData(no):
    return no * 2

def ReduceData(a, b):
    max_value = a
    if b > max_value:
        max_value = b
    return max_value

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