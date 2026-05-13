class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
                accomp = target - val

                if accomp in seen:
                        return [seen[accomp], i]
                
                seen[val] = i