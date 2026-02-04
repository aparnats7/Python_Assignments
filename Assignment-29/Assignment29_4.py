import sys
import os

def CompareFiles(fileName1, fileName2):    
    Result = os.path.exists(fileName1)
    
    if(Result == False):
        print("There is no such file")
        return
    
    fobj1 = open(fileName1, "r")
    Data1 = fobj1.read()   
           
    fobj2 = open(fileName2,"r")
    Data2 = fobj2.read()
    
    if(Data1 == Data2):
        print("Success")
        
    else:
        print("Failure")
    
    fobj1.close()
    fobj2.close()
        
def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        
        return
    
    CompareFiles(sys.argv[1], sys.argv[2])
    
if __name__ == "__main__":
    main()