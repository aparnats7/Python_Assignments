# Write a program which accept character from user and check whether it is vowel or consonant.

def ChkVowel(ch):
    vowels = "AEIOUaeiou"
    
    for i in vowels:
        if i == ch:
            return True

    return False 
        
def main():
    print("Enter Character :")   
    char = input()
    
    ret = ChkVowel(char)
    
    if ret == True:
        print("Vowel")
        
    else:
        print("Consonant")
    
if __name__ == "__main__":
    main()