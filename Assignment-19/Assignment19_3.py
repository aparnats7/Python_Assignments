# Write a program which accepts list of numbers from user and filters 
# that numbers which are between 70 and 90. After that add 10 to each
# filtered number. Finally multiply all the modified numbers.   

import functools

FilterData = lambda no : no >= 70 and no <= 90

MapData = lambda no : no + 10

ReduceData = lambda a, b : a * b

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