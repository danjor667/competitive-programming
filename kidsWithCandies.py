class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        res = []
        for candie in candies:
            if candie + extraCandies >= max_candie:
                res.append(True)
            else:
                res.append(False)
        return res
