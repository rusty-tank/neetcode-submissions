class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        vol = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(height[l], max_l)
                vol += max_l - height[l]
            else:
                r -= 1
                max_r = max(height[r], max_r)
                vol += max_r - height[r]
        return vol