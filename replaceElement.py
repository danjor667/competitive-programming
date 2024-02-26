
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i

        for a, b in operations:
            nums[my_dict.get(a)] = b
            my_dict[b] = my_dict.get(a)
        return nums
