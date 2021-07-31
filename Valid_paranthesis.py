'''Problem : Valid Parathesis '''

#CODE :

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = ['()', '[]', '{}']
        flag = False
        while len(s) > 0:
            i = 0
            while i < 3:
                if parentheses[i] in s:
                    s = s.replace(parentheses[i], '')
                    i = 0
                    flag = True
                else:
                    i += 1
            if len(s) == 0:
                return True
            else:
                flag = False
                break
        return False
