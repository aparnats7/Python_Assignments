# Write a program which accepts marks of a student and display the grade according to the following criteria:

def DisplayGrades(marks):
    if marks >= 75:
        print("Distinction")
        
    elif marks >= 60:
        print("First Class")
        
    elif marks >= 50:
        print("Second Class")
        
    elif marks < 50:
        print("Fail")
        
    else:
        print("Invalid input")
        
def main():
    print("Enter marks :")
    data = int(input())
    
    DisplayGrades(data)
    
if __name__ == "__main__":
    main()