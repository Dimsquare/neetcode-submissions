from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup = Counter(s1)
        l = 0
        r = 0
        while r<=len(s2):
            if Counter(s2[l:r])==lookup:
                return True
            elif len(s2[l:r])>=len(s1):
                l+=1
            r+=1
        return False
