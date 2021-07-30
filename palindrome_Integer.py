'''Problem : Palindrome Integer '''

#CODE :

class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = str(x)[::-1]
        print("palindrome:", palindrome)
        if palindrome == str(x):
            return True
        else: 
            return False
        
