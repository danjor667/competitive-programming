class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        n = min(len(word1), len(word2))
        i = 0
        while i < n:
            string += word1[i]
            string += word2[i]
            i += 1
        if len(word1) > len(word2):
            string += word1[n:]
        else:
            string += word2[n:]
        return string
