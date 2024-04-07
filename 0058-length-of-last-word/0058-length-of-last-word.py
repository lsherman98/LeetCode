class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
#         p = len(s) - 1
        
#         while s[p] == ' ':
#             p -= 1
        
#         count = 0
#         while p >= 0 and s[p] != ' ':
#             count += 1
#             p -= 1
            
#         return count
    