class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        b=bin(n)[2:]
        count = b.count('1') 
        return count