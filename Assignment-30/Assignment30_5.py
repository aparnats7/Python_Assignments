import sys
import os

def ChkWord(fileName, word):    
    Result = os.path.exists(fileName)
    
    if(Result == False):
        print("There is no such file")
        return
    
    fobj1 = open(fileName, "r")
    Data = fobj1.read()
    fobj1.close()
    
    temp = ""

    for ch in Data:
        if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
            temp = temp + ch
        else:
            if temp == word:
                print(word, "is present in the file")
                return
            temp = ""

    if temp == word:
        print(word, "is present in the file")
        return

    print(word, "is not present in the file")
        
def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        
        return
    
    ChkWord(sys.argv[1], sys.argv[2])
    
if __name__ == "__main__":
    main()