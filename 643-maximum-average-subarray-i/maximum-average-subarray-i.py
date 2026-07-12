class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        curr=sum(nums[:k])
        max_=curr
        for i in range(k,n):
            curr=curr+nums[i]-nums[i-k]
            if curr>max_:
                max_=curr
        return max_/k
            
            
        