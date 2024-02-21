class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        my_dict = {}
        
        for char in t:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        for char in s:
            if my_dict.get(char) == 1:
                del my_dict[char]
            else:
                my_dict[char] -= 1
        return list(my_dict.keys())[0]
