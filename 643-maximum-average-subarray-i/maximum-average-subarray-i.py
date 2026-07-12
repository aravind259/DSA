class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        curr=sum(nums[:k])
        max_avg=curr/k
        for i in range(k,n):
            curr+=nums[i]
            curr-=nums[i-k]
            avg=curr/k
            max_avg=max(max_avg,avg)
        return max_avg

        