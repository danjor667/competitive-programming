class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = list(set(list1) & set(list2))
        lower = float(inf)
        res = []
        for ele in common:
            first = list1.index(ele)
            second = list2.index(ele)
            _sum = first + second
            if _sum < lower:
                if len(res) != 0:
                    res.pop()
                res.append(list1[list1.index(ele)])
                lower = _sum
            elif _sum == lower:
                res.append(list1[list1.index(ele)])
        return res
