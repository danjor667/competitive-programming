class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        while i < ceil(n/2):
            s[i], s[n-1-i] = s[n-1-i], s[i]
            i += 1
