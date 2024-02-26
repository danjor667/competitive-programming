class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        A.sort()
        B.sort()
        for pair in zip(A,B):
            if pair[0] != pair[1]:
                return False
        return True
