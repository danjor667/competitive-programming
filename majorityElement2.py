class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = {}
        res = []
        for ele in nums:
            if ele in my_dict:
                my_dict[ele] += 1
            else:
                my_dict[ele] = 1
        for k, v in my_dict.items():
            if v > len(nums) / 3:
                res.append(k)
        return res
