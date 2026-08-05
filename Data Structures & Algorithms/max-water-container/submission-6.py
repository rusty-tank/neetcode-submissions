class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        hvol = 0

        while l < r:
            vol = min(heights[l], heights[r]) * (r - l)
            hvol = max(vol, hvol)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return hvol
            