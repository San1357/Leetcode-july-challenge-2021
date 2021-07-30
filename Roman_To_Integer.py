'''Problem : Roman  To Integer '''
#CODE :

class Solution:
    def romanToInt(self, s: str) -> int:        
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M': 1000}
        n = len(s)
        num = dict[s[n-1]] 
        for i in range(n-2, -1, -1):
            if dict[s[i]]>= dict[s[i+1]]:
                num += dict[s[i]]
            else: 
                num -= dict[s[i]]
        return num
