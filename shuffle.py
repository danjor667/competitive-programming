class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        x, y = 0, len(nums)//2
        for i in range(y):
            res.append(nums[x])
            res.append(nums[y])
            x += 1
            y += 1
        return res
