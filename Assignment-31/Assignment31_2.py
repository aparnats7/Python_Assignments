import os
import sys
import time

def DirectoryRename(DirName, OldExt, NewExt):
    Border = "-" * 50
    TimeStamp = time.ctime()
    
    LogFileName = "Marvellous%s.log" % (TimeStamp)
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")
    
    fobj = open(LogFileName, "w")
    
    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a directory rename script\n")
    fobj.write(Border + "\n")
    
    Ret = os.path.exists(DirName)
    
    if(Ret == False):
        print("There is no such directory\n")
        fobj.write("Directory not found\n")
        fobj.close()
        return
    
    Ret = os.path.isdir(DirName)
    
    if(Ret == False):
        print("It is not a Directory\n")
        fobj.write("Given path is not a directory\n")
        fobj.close()
        return
    
    RenameCount = 0
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(OldExt):
                OldPath = os.path.join(FolderName, fname)
                
                NewName = fname.replace(OldExt, NewExt)
                NewPath = os.path.join(FolderName, NewName)
                
                os.rename(OldPath, NewPath)
                RenameCount = RenameCount + 1
                
                fobj.write("Renamed file : " + fname + " -> " + NewName + "\n")
    
    fobj.write(Border + "\n")
    fobj.write("Total files renamed : " + str(RenameCount) + "\n")
    fobj.write("Log file created at : " + TimeStamp + "\n")
    fobj.write(Border + "\n")
    
    fobj.close()

def main():
    
    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        print("Usage : Application_Name Directory_Name Old_Extension New_Extension")
        return
    
    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()