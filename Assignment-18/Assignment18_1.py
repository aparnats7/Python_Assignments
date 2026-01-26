# Write a program which accepts N numbers from user and store them into List. Return addition of all elements from that List.

def Add(a, b):
    return a + b

def main():
    
    list = []
    n = int(input("Enter number of elements : "))
    print("Enter elements : ")
    
    for i in range(0, n):
        element = int(input())
        list.append(element)

    total = 0
    for i in range(0, n):
        total = Add(total, list[i])
        
    print(total)

if __name__ == "__main__":
    main()