import os
import sys
import time
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1000)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)
        
    fobj.close()
    
    return hobj.hexdigest()

def DirectoryChecksum(DirName):
    Border = "-" * 50
    TimeStamp = time.ctime()

    LogFileName = "Marvellous%s.log" % TimeStamp
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    fobj = open(LogFileName, "w")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("Directory Checksum Log\n")
    fobj.write(Border + "\n")

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        fobj.write("Directory not found\n")
        fobj.close()
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        fobj.write("Given path is not a directory\n")
        fobj.close()
        return

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            Checksum = CalculateChecksum(fname)
            fobj.write("File name : " + fname + " Checksum : " + Checksum + "\n")

    fobj.write(Border + "\n")
    fobj.write("Log created at : " + TimeStamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage : Application_Name Directory_Name")
        return

    DirectoryChecksum(sys.argv[1])

if __name__ == "__main__":
    main()