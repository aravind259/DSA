class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack=[]
        ans=0
        for ch in s:
            while ch in stack:
                stack.pop(0) 
            stack.append(ch)
            ans = max(ans, len(stack))

        return ans