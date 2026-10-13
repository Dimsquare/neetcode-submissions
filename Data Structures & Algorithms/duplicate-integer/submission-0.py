from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_counter = Counter(nums)
        for num in nums_counter.values():
            if num>1:
                return True
        return False