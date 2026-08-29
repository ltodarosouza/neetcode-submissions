class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}
        if len(s) != len(t):
            return False
        for l in s:
            if l in str1:
                str1[l] += 1
            else:
                str1[l] = 1
        for l in t:
            if l in str2:
                str2[l] += 1
            else:
                str2[l] = 1
        if str1 == str2:
            return True
        return False
            
        