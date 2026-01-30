class Demo:
    Value = 0
    
    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b
        
    def Fun(self):
        print("Value of no1 is : ", self.no1)
        print("Value of no2 is : ", self.no2)
        
    def Gun(self):
        print("Value of no1 is : ", self.no1)
        print("Value of no2 is : ", self.no2)
        
def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)
    
    obj1.Fun()
    obj2.Fun()
    
    obj1.Gun()
    obj2.Gun()
    
if __name__ == "__main__":
    main()
        