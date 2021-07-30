'''Problem : REverse Integer '''

#CODE :

class Solution:
    def reverse(self, x: int) -> int:
        my_reverse = str(abs(x))
        my_reverse = my_reverse[::-1]
        
        my_reverse = int(my_reverse)
        if my_reverse >= 2**31 -1 or my_reverse <= -2**31:
            return 0
        elif x < 0:
            return -1* my_reverse
        else: 
            return my_reverse
