'''PRoblem : Longest Common Prefix '''

#CODE :

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i in range(len(strs[0])):
            print("i", i)
            for string in strs[1:]:
                print("String",string)
                print("len_Str", len(string))
                print("string_i", string[i])
                print("strs[0][i]", strs[0][i])
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
