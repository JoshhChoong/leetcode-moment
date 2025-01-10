from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1occurences = Counter(s1)
        s1len = len(s1)
        l = 0
        r = len(s1)


        for l in range(len(s2)):
            try:
                if Counter(s2[l:r]) == s1occurences:
                    return True
            except:
                return False
            r += 1
        return False