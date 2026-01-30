class Circle:
    PI = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        
    def Accept(self):
        print("Enter the Radius of Circle :")
        
        self.Radius = float(input())    
    
    def CalculateArea(self):
        self.Area = self.PI * (self.Radius ** 2)
        
        return self.Area
    
    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius
        
        return self.Circumference
        
    def Display(self):
        print("Radius of Circle is : ",self.Radius)
        
        self.ret1 = self.CalculateArea()
        print("Area of Circle is : ", self.ret1)
        
        self.ret2 = self.CalculateCircumference()
        print("Circumference of Circle is : ", self.ret2)
    
def main():
    obj1 = Circle()
    obj2 = Circle()
    
    obj1.Accept()
    obj1.CalculateArea()   
    obj1.CalculateCircumference()
    obj1.Display()
    
    obj2.Accept()
    obj2.CalculateArea() 
    obj2.CalculateCircumference()
    obj2.Display()
    
if __name__ == "__main__":
    main()