import threading

def Sum(lst):
    total = 0
    
    for i in lst:
        total = total + i
        
    print("Sum of elements is:", total)

def Product(lst):
    result = 1
    
    for i in lst:
        result = result * i
        
    print("Product of elements is:", result)

def main():
    lst = []
    
    n = int(input("Enter number of elements: "))
    print("Enter elements:")
    
    for i in range(n):
        lst.append(int(input()))
        
    t1 = threading.Thread(target=Sum, args=(lst,))
    t2 = threading.Thread(target=Product, args=(lst,))
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()