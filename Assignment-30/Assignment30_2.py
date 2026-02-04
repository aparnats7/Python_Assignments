import sys
import os

def CountWords(fileName):    
    Result = os.path.exists(fileName)
    
    if(Result == False):
        print("There is no such file")
        return
    
    fobj1 = open(fileName, "r")
    
    Data = fobj1.read()
    fobj1.close()
    
    cnt = 0
    word = ""

    for ch in Data:
        if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
            word = word + ch
            
        else:
            if word != "":
                cnt += 1
                word = ""

    if word != "":
        cnt += 1

    return cnt
        
def main():
    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        
        return
    
    Ret = CountWords(sys.argv[1])
    
    print("Total number of words in the file is : ", Ret)
    
if __name__ == "__main__":
    main()