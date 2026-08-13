class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: odd length strings can never be balanced
        if len(s) % 2 != 0:
            return False
            
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack is non-empty, else use a dummy character
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches
                if bracket_map[char] != top_element:
                    return False
            else:
                # Character is an opening bracket; push to stack
                stack.append(char)
                
        # If the stack is empty, all brackets were correctly matched
        return len(stack) == 0