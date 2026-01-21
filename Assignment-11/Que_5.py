# Palindrome Number Check

def ChkPalindrome(no):
    rev = 0
    
    while no > 0:
        digit = no % 10
        
        rev = (rev * 10) + digit
        
        no = no // 10
        
    return rev

def main():
    print("Enter number :")
    value = int(input())
    
    ret = ChkPalindrome(value)
    
    if ret == value:
        print("Palindrome Number")
        
    else:
        print("Not a Palindrome Number")
    
if __name__ == "__main__":
    main()