from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        res = []
        print(count)
        sorted_keys = sorted(count, key=count.get, reverse=True)
        return sorted_keys[:k]
        