import sys
import os

def CountLine(fileName):    
    Result = os.path.exists(fileName)
    
    if(Result == False):
        print("There is no such file")
        return
    
    fobj1 = open(fileName, "r")

    for line in fobj1:
        print(line)
        
def main():
    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        
        return
    
    CountLine(sys.argv[1])
    
if __name__ == "__main__":
    main()