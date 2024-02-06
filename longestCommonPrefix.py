class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for word in strs:
            temp = ""
            for pair in zip(ans, word):
                if pair[0] == pair[1]:
                    temp += pair[0]
                else:
                    ans = temp
                    break
            ans = temp
        return ans
