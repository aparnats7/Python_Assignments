import os

def ChkFile(fileName):
    Ret = os.path.exists(fileName)
    
    if(Ret == True):
        fobj = open(fileName, "r")
        print("File gets successfully opened")
    
    else:
        print("There is no such file")

def main():
    fileName = input("Enter the file name : ")
    
    ChkFile(fileName)
    
if __name__ == "__main__":
    main()