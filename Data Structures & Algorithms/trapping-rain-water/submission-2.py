class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        vol = 0
        
        while l < r:
            # Always process the side with the smaller max height boundary
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                vol += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                vol += right_max - height[r]
                
        return vol