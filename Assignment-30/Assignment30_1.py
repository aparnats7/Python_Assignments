import sys
import os

def CountLine(fileName):    
    Result = os.path.exists(fileName)
    
    if(Result == False):
        print("There is no such file")
        return
    
    fobj1 = open(fileName, "r")
    
    Data = fobj1.read()
    fobj1.close()
    
    cnt = 0

    for ch in Data:
        if ch == '\n':
            cnt = cnt + 1

    if(len(Data) > 0):
        return cnt + 1
        
    else:
        return cnt
        
def main():
    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        
        return
    
    Ret = CountLine(sys.argv[1])
    
    print("Total number of lines in the file is : ", Ret)
    
if __name__ == "__main__":
    main()