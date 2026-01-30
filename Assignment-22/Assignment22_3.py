class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        
    def Accept(self):
        print("Enter first number : ")
        self.Value1 = int(input())
        
        print("Enter second number : ")
        self.Value2 = int(input())
        
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            print("Division by zero is not possible")
            
        else:
            return self.Value1 / self.Value2
    
def main():
    Obj1 = Arithmetic()
    Obj2 = Arithmetic()

    print("Enter values for first object:")
    Obj1.Accept()

    print("Addition:", Obj1.Addition())
    print("Subtraction:", Obj1.Subtraction())
    print("Multiplication:", Obj1.Multiplication())
    print("Division:", Obj1.Division())

    print("\nEnter values for second object:")
    Obj2.Accept()

    print("Addition:", Obj2.Addition())
    print("Subtraction:", Obj2.Subtraction())
    print("Multiplication:", Obj2.Multiplication())
    print("Division:", Obj2.Division())


if __name__ == "__main__":
    main()