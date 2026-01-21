# Program to find area of circle

def AreaOfCircle(r):
    area = (22/7) * r * r
    
    return area

def main():
    print("Enter the radius :")
    radius = int(input())
    
    ret = AreaOfCircle(radius)
    
    print("Area of the circle is : ",ret)
    
if __name__ == "__main__":
    main()