class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        collect = {}
        collect2 = {}
        for c in s:
            if c in collect:
                collect[c] += 1
            else:
                collect[c] = 1
        for c in t:
            if c in collect2:
                collect2[c] += 1
            else:
                collect2[c] = 1

        return collect == collect2