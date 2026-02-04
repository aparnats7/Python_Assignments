
def ReadData(fileName):
    try:
        fobj = open(fileName, "r")
        print("File gets successfully opened")
        
        Data = fobj.read()
        
        print("Data from file is : ",Data)
        
        fobj.close()
        
    except FileNotFoundError:
        print("Unable to open file as there is no such file")
        
    finally:
        print("End of application")
        
def main():
    fileName = input("Enter the name of the file : ")
    
    ReadData(fileName)
    
if __name__ == "__main__":
    main()