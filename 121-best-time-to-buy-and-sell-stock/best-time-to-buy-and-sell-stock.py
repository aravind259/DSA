class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        ma=prices[0]
        pro=0
        for i in range(1,n):
            ma=min(ma,prices[i])
            pr=prices[i]-ma
            pro=max(pro,pr)
        return pro


       