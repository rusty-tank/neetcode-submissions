# from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        clusters = []
        stack = nums
        while stack:
            curr = stack.pop(0)
            if len(clusters) < 1:
                clusters.append([curr])
            else:
                if clusters[-1][-1] + 1 >= curr:
                    if curr not in clusters[-1]:
                        clusters[-1].append(curr)
                    else:
                        continue
                else:
                    clusters.append([curr])
        resarr = []
        res = 0
        for v in clusters:
            resarr.append(len(v))
        if not resarr:
            return 0
        else:
            return max(max(resarr), res)
