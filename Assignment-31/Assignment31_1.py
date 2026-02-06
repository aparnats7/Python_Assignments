import os
import sys
import time

def DirectoryFileSearch(DirName, Ext):
    Border = "-" * 50
    TimeStamp = time.ctime()

    LogFileName = "Marvellous%s.log" % (TimeStamp)
    LogFileName = LogFileName.replace(" ", "_").replace(":", "_")

    fobj = open(LogFileName, "w")

    fobj.write(Border + "\n")
    fobj.write("Directory File Search Log\n")
    fobj.write(Border + "\n")

    if not os.path.exists(DirName):
        fobj.write("Directory not found\n")
        return

    if not os.path.isdir(DirName):
        fobj.write("Given name is not a directory\n")
        return

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(Ext):
                fobj.write(fname + "\n")

    fobj.write(Border + "\n")
    fobj.write("Log created at : " + TimeStamp + "\n")
    fobj.close()

def main():
    if len(sys.argv) != 3:
        print("Invalid arguments")
        return

    DirectoryFileSearch(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
