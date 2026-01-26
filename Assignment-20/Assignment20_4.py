import threading

def ChkLower(s):
    str1 = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    
    for ch in s:
        if ch in str1:
            count = count + 1
            
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of lowercase characters :", count)
        
        
def ChkUpper(s):
    str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    
    for ch in s:
        if ch in str2:
            count = count + 1
            
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of uppercase characters :", count)
    
    
def ChkDigit(s):
    str3 = "0123456789"
    count = 0
    
    for ch in s:
        if ch in str3:
            count = count + 1
            
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of digits :", count)
    
    
def main():
    print("Enter the String : ")
    s = input()
    
    Small = threading.Thread(target=ChkLower, args=(s,), name="Small")
    Capital = threading.Thread(target=ChkUpper, args=(s,), name="Capital")
    Digit = threading.Thread(target=ChkDigit, args=(s,), name="Digits")
    
    Small.start()
    Capital.start()
    Digit.start()
    
    Small.join()
    Capital.join()
    Digit.join()
    
    
if __name__ == "__main__":
    main()
