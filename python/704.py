import math 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bSearch(l,h):
            cur = math.floor((h + l) / 2)
            if target == nums[cur]:
                return cur
            elif cur == l:
                return -1
            elif target < nums[cur]:
                return bSearch(l,cur)
            elif target > nums[cur]:
                return bSearch(cur,h)
        return bSearch(0,len(nums))