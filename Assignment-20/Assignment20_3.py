import threading

def ChkEven(no):
    eList = []
    sum = 0
    
    for i in range(1, len(no) + 1):
        if i % 2 == 0:
            eList.append(i)
            
    for i in eList:
        sum = sum + i
        
    print(sum)
    
def ChkOdd(no):
    oList = []
    total = 0
    
    for i in range(1, len(no) + 1):
        if i % 2 != 0:
            oList.append(i)
    
    for i in oList:
        total = total + i
        
    print(total)
    
def main():
    lst = []
    
    print("Enter number of elements : ")
    n = int(input())
    
    print("Enter elements : ")
    
    for i in range(0, n):
        value = int(input())

        lst.append(value)
    
    EvenList = threading.Thread(target=ChkEven, args=(lst,))
    
    OddList = threading.Thread(target=ChkOdd, args=(lst,))
    
    EvenList.start()
    OddList.start()
    
    EvenList.join()
    OddList.join()

if __name__ == "__main__":
    main()