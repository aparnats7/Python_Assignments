# Write a program which accepts N numbers from user and store them into List and return minimum number from that List.

def MinElement(data):
    min_value = data[0]
    for i in range(1, len(data)):
        if data[i] < min_value:
            min_value = data[i]
    return min_value

def main():
    
    list = []
    n = int(input("Enter number of elements : "))
    print("Enter elements : ")
    
    for i in range(0, n):
        element = int(input())
        list.append(element)

    ret = MinElement(list)
    print(ret)
    
if __name__ == "__main__":
    main()

