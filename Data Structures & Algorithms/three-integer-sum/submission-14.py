class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = set()
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    sols.add((nums[i], nums[l], nums[r]))
                    l += 1
                if sum > 0:
                    r -= 1
                if sum < 0:
                    l += 1
        return [list(t) for t in sols]
