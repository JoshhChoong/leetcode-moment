class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        targets = set(s)
        seth = set()
        ans = 0
        for target in targets:
            l = 0
            replacement = 0
            for r,e in enumerate(s):
                seth.add(e)
                if e != target:
                    replacement += 1

                while replacement > k:
                    if l == len(s) - 1:
                        break
                    if s[l] != target:
                        replacement -= 1
                    l += 1
                ans = max(ans,r - l + 1)
            seth.clear()

        return ans
