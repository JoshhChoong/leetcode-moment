class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        count = 0
        
        for pos,temp in enumerate(temperatures):

            while stack:
                if temp > stack[-1][0]:
                    ans[stack[-1][1]] = (pos-stack[-1][1])
                    stack.pop()
                    count += 1
                else: break

            stack.append([temp,pos])
        
        return ans