import threading

def ChkPrime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def ChkPrime(lst):
    print("Prime numbers are:")
    for no in lst:
        if ChkPrime(no):
            print(no, end=" ")
    print()

def ChkNonPrime(lst):
    print("Non-prime numbers are:")
    for no in lst:
        if not ChkPrime(no):
            print(no, end=" ")
    print()

def main():
    lst = []
    
    n = int(input("Enter number of elements: "))
    print("Enter elements:")
    
    for i in range(n):
        lst.append(int(input()))
        
    Prime = threading.Thread(target=ChkPrime, args=(lst,), name="Prime")
    NonPrime = threading.Thread(target=ChkNonPrime, args=(lst,), name="NonPrime")
    
    Prime.start()
    Prime.join()
    
    NonPrime.start()  
    NonPrime.join()

if __name__ == "__main__":
    main()
