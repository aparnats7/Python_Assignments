# Write a program which accepts N numbers from user and store them into List and return frequency of particular number from that List.

def Frequency(list, no):
    count = 0
    for i in range(0, len(list)):
        if(list[i] == no):
            count = count + 1
    return count

def main():
    
    list = []
    n = int(input("Enter number of elements : "))
    print("Enter elements : ")
    
    for i in range(0, n):
        element = int(input())
        list.append(element)

    num = int(input("Enter number to check frequency : "))
    
    ret = Frequency(list, num)
    print(ret)
    
if __name__ == "__main__":
    main()