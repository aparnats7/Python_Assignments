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

def FindDuplicate(Path = "Marvellous"):
    MyDict = {}

    for FolderName, SubFolder, FileName in os.walk(Path):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)

            if checksum in MyDict:
                MyDict[checksum].append(fname)
            else:
                MyDict[checksum] = [fname]

    return MyDict

def CreateLogFile():
    TimeStamp = time.ctime()
    LogFileName = "Marvellous%s.log" % TimeStamp
    LogFileName = LogFileName.replace(" ", "_").replace(":", "_")
    return open(LogFileName, "w")

def DeleteDuplicate(Path = "Marvellous"):
    if not os.path.isdir(Path):
        print("Invalid directory")
        return

    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    fobj = CreateLogFile()

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1

            if(Count > 1):
                print("Deleted File :", subvalue)
                fobj.write("Deleted File : " + subvalue + "\n")
                os.remove(subvalue)
                Cnt = Cnt + 1

        Count = 0

    fobj.write("Total deleted files : " + str(Cnt) + "\n")
    fobj.close()

    print("Total deleted files :", Cnt)

def main():
    if len(sys.argv) != 2:
        print("Invalid arguments")
        return

    DeleteDuplicate(sys.argv[1])

if __name__ == "__main__":
    main()