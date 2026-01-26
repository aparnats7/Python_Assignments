
import threading

def Factors(no):
    flist = []
    for i in range(1, no):
        if no % i == 0:
            flist.append(i)
    return flist
        
def ChkEvenFactor(no):
    sum = 0
    
    ret = Factors(no)
    
    for i in ret:
        if i % 2 == 0:
            sum = sum + i
    print(sum)
    
def ChkOddFactor(no):
    sum = 0
    
    ret = Factors(no)
    
    for i in ret:
        if i % 2 != 0:
            sum = sum + i
    print(sum)
    
def main():
    print("Enter number : ")
    value = int(input())
    
    EvenFactor = threading.Thread(target=ChkEvenFactor, args=(value,))
    OddFactor = threading.Thread(target=ChkOddFactor, args=(value,))
    
    EvenFactor.start()
    EvenFactor.join()
    
    OddFactor.start()    
    OddFactor.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()