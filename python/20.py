class Solution:
    def isValid(self, s: str) -> bool:
        steven = []
        deniz = {"(":")", "[":"]","{":"}",}

        for char in s:
            if char in deniz.keys():
                    steven.append(char)
            else:
                if len(steven) == 0:
                    return False
                elif char == deniz[steven[-1]]:
                    steven.pop()
                else:
                    return False

        return True if not steven else False