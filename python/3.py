class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seth = set()
        l = 0
        ans = 0

        for r,e in enumerate(s):
            while e in seth:
                seth.remove(s[l])
                l += 1
            seth.add(e)
            ans = max(ans, len(seth))
        return ans