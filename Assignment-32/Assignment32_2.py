import hashlib
import os
import sys
import time

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

def CreateLogFile():
    TimeStamp = time.ctime()
    LogFileName = "Marvellous%s.log" % TimeStamp
    LogFileName = LogFileName.replace(" ", "_").replace(":", "_")
    return open(LogFileName, "w")

def FindDuplicate(DirectoryName):
    if not os.path.isdir(DirectoryName):
        print("Invalid directory")
        return {}

    Duplicate = {}

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            path = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(path)

            if checksum in Duplicate:
                Duplicate[checksum].append(path)
            else:
                Duplicate[checksum] = [path]

    return Duplicate

def WriteDuplicateLog(Duplicate):
    fobj = CreateLogFile()

    for value in Duplicate.values():
        if len(value) > 1:
            for fname in value:
                fobj.write(fname + "\n")

    fobj.close()

def main():
    if len(sys.argv) != 2:
        print("Invalid arguments")
        return

    Result = FindDuplicate(sys.argv[1])
    WriteDuplicateLog(Result)

if __name__ == "__main__":
    main()