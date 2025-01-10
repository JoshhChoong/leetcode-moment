from math import ceil
class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        ans = 0

        while l <= r:
            count = 0
            m = (l + r) // 2

            for item in piles:
                count += math.ceil(item / m)

            if count <= h:
                if l <= r:
                    ans = m
                r = m - 1
            else:
                l = m + 1

        return ans

        # for i in range(1,r):
        #     count = 0
        #     for item in piles:
        #         count += math.ceil(item / i)
        #         if count > h:
        #             break
        #     if count <= h:
        #         return i
        # return r