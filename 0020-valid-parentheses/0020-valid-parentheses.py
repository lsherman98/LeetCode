class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closedToOpen = {')' : '(', ']' : '[', '}' : '{'}
        
        for c in s:
            if c in closedToOpen:
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
        