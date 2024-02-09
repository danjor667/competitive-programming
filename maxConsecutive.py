class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        for ele in nums:
            if ele == 1:
                count += 1
            else:
                maximum = max(count, maximum)
                count = 0
        maximum = max(count, maximum)
        return maximum
        
