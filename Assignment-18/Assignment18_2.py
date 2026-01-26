# Write a program which accepts N numbers from user and store them into List and return maximum number from that List.

def MaxElement(data):
    max_value = data[0]
    for i in range(1, len(data)):
        if data[i] > max_value:
            max_value = data[i]
    return max_value

def main():
    
    list = []
    n = int(input("Enter number of elements : "))
    print("Enter elements : ")
    
    for i in range(0, n):
        element = int(input())
        list.append(element)

    ret = MaxElement(list)
    print(ret)
    
if __name__ == "__main__":
    main()