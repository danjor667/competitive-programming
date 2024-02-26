class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won ={}
        lost = {}
        only_wins = []
        one_lost = []
        for match in matches:
            won[match[0]] = won[match[0]] + 1 if match[0] in won else 1
            lost[match[1]] = lost[match[1]] + 1 if match[1] in lost else 1
        for ele in won:
            if ele not in lost:
                only_wins.append(ele)
        for ele in lost:
            if lost.get(ele) == 1:
                one_lost.append(ele)
        return [sorted(only_wins), sorted(one_lost)]
