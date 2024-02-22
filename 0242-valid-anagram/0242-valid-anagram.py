class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        scounts = {}
        tcounts = {}

        for char in s:
            if char in scounts:
                scounts[char] += 1
            else: 
                scounts[char] = 1

        for char in t:
            if char in tcounts:
                tcounts[char] += 1
            else: 
                tcounts[char] = 1

        return scounts == tcounts 
        