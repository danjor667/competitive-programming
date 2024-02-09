class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        my_dict = {}
        count = 0
        for ele in nums:
            if ele in my_dict:
                count += my_dict[ele]
                my_dict[ele] += 1
            else:
                my_dict[ele] = 1
        return count
