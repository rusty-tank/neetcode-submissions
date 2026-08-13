class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_map:
                current = stack.pop() if stack else '#'
                if current not in bracket_map[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0