# Program to find area of rectangle

def AreaOfRectangle(l,w):
    area = l * w
    
    return area

def main():
    print("Enter the length :")
    length = int(input())
    
    print("Enter the width :")
    width = int(input())
    
    ret = AreaOfRectangle(length, width)
    
    print("Area of the rectangle is : ",ret)
    
if __name__ == "__main__":
    main()