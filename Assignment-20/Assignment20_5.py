import threading

def Sequence():
    for i in range(1, 51):
        print(i)

def ReverseSequence():
    for i in range(50, 0, -1):
        print(i)
        
def main():
    Thread1 = threading.Thread(target=Sequence)
    Thread2 = threading.Thread(target=ReverseSequence)
    
    Thread1.start()
    Thread1.join()
    
    Thread2.start()    
    Thread2.join()
    
if __name__ == "__main__":
    main()