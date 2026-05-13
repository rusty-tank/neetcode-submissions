class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        collect = {}
        for c in s:
            if c in collect:
                collect[c] += 1
            else:
                collect[c] = 1
        for c in t:
            if c in collect:
                collect[c] -= 1
            else:
                return False

        for val in collect.values():
            if val != 0:
                return False
        return True