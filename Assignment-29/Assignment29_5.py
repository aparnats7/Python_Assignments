import sys
import os

def CountFrequency(fileName, string):    
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
        if ch == ' ' or ch == '\n' or ch == '.':
            if word == string:
                cnt = cnt + 1
            word = ""
        else:
            word = word + ch

    if word == string:
        cnt = cnt + 1
        
    return cnt
        
def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        
        return
    
    Ret = CountFrequency(sys.argv[1], sys.argv[2])
    
    print("Frequency of the given string in the file is : ", Ret)
    
if __name__ == "__main__":
    main()