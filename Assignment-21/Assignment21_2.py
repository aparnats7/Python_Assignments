import threading

def Maximum(lst):
    max_no = lst[0]
    
    for i in lst:
        if i > max_no:
            max_no = i
            
    print("Maximum element is:", max_no)

def Minimum(lst):
    min_no = lst[0]
    
    for i in lst:
        if i < min_no:
            min_no = i
            
    print("Minimum element is:", min_no)

def main():
    lst = []
    
    n = int(input("Enter number of elements: "))
    print("Enter elements:")
    
    for i in range(n):
        lst.append(int(input()))
        
    Thread1 = threading.Thread(target=Maximum, args=(lst,))
    Thread2 = threading.Thread(target=Minimum, args=(lst,))
    
    Thread1.start()
    Thread1.join()
    
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()