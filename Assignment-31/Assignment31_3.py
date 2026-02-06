import os
import sys
import time
import shutil

def DirectoryCopy(SrcDir, DestDir):
    Border = "-" * 50
    TimeStamp = time.ctime()
    
    LogFileName = "Marvellous%s.log" % (TimeStamp)
    LogFileName = LogFileName.replace(" ", "_").replace(":", "_")
    
    fobj = open(LogFileName, "w")
    
    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a directory copy script\n")
    fobj.write(Border + "\n")
    
    if not os.path.isdir(SrcDir):
        print("Source directory not found")
        fobj.write("Source directory not found\n")
        fobj.close()
        return
    
    if not os.path.exists(DestDir):
        os.mkdir(DestDir)
        fobj.write("Destination directory created\n")
    
    FileCount = 0
    
    for FolderName, SubFolder, FileName in os.walk(SrcDir):
        for fname in FileName:
            SrcPath = os.path.join(FolderName, fname)
            DestPath = os.path.join(DestDir, fname)
            shutil.copy2(SrcPath, DestPath)
            FileCount = FileCount + 1
            fobj.write("Copied file : " + fname + "\n")
    
    fobj.write(Border + "\n")
    fobj.write("Total files copied : " + str(FileCount) + "\n")
    fobj.write("Log created at : " + TimeStamp + "\n")
    fobj.write(Border + "\n")
    
    fobj.close()

def main():
    
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage : Application_Name Source_Directory Destination_Directory")
        return
    
    DirectoryCopy(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()