from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        
        for i, v in enumerate(nums):
            d[v] += 1
        
        sorted_key = sorted(d, key=d.get, reverse=True)
        return sorted_key[:k]