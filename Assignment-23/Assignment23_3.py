class Numbers:
    def __init__(self, Value):
        self.Value = Value
        
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True   
            
    def ChkPerfect(self):
        self.sum = 0
        
        for i in range(1, self.Value):
            if self.Value % i == 0:
                self.sum = self.sum + i
                
        if self.sum == self.Value:
            return True
        else:
            return False
        
    def Factors(self):
        print("Factors:", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()
                
    def SumFactors(self):
        sum = 0
        
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i
                
        return sum
    

def main():
    print("Enter number for object 1 : ")
    no1 = int(input())
    obj1 = Numbers(no1)

    print("Enter number for object 2 : ")
    no2 = int(input())
    obj2 = Numbers(no2)

    print("Enter number for object 3 : ")
    no3 = int(input())
    obj3 = Numbers(no3)
    
    print("Object 1:")
    print("Is Prime:", obj1.ChkPrime())
    print("Is Perfect:", obj1.ChkPerfect())
    print("Factors are : ",obj1.Factors())
    print("Sum of Factors:", obj1.SumFactors())
    
    print("Object 2:")
    print("Is Prime:", obj2.ChkPrime())
    print("Is Perfect:", obj2.ChkPerfect())
    print("Factors are : ",obj2.Factors())
    print("Sum of Factors:", obj2.SumFactors())
    
    print("Object 3:")
    print("Is Prime:", obj3.ChkPrime())
    print("Is Perfect:", obj2.ChkPerfect())
    print("Factors are : ",obj3.Factors())
    print("Sum of Factors:", obj3.SumFactors())

    
if __name__ == "__main__":
    main()
