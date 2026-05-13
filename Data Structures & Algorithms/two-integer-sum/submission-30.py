class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ele = {}

        for i, num in enumerate(nums):
            if num not in ele:
                ele[num] = [i]
            else:
                ele[num].append(i)

        for i, num in enumerate(nums):
            accomp = target - num

            ele[num].remove(i)

            if accomp in ele and len(ele[accomp]) > 0:
                return [i, ele[accomp][0]]

            ele[num].append(i)