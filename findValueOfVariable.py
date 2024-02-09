class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        my_dict = {"X++": 1, "++X": 1, "--X": -1, "X--": -1}
        x = 0
        for operation in operations:
            x += my_dict[operation]
        return x
