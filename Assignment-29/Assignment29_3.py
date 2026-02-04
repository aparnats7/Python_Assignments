import sys
import os

def CopyFileData(fileName1):    
    Result = os.path.exists(fileName1)
    
    if(Result == False):
        print("There is no such file")
        return
    
    fobj1 = open(fileName1, "r")
    
    Data = fobj1.read()
    
    fobj1.close()
        
    fobj2 = open("Demo.txt","w")
    fobj2.write(Data)
    
    print("The Content of the file get successfully copied into the Demo.txt")
    
    fobj2.close()
        
def main():
    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        
        return
    
    CopyFileData(sys.argv[1])
    
if __name__ == "__main__":
    main()