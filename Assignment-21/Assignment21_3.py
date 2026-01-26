import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter
    for i in range(1000):
        lock.acquire()
        counter = counter + 1
        lock.release()

def main():
    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)
    t3 = threading.Thread(target=Increment)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print("Final value of counter:", counter)

if __name__ == "__main__":
    main()