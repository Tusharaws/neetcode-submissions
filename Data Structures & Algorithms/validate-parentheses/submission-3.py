class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(','}':'{',']':'['}
        stack = []
        for ch in s:
            if  ch in valid:
                top_element = stack.pop() if stack else "#"
                if valid[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        return len(stack)==0