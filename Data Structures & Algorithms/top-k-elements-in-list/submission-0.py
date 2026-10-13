from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        return_value = frequency.most_common(k)
        return_list = []
        for n in return_value:
            a, _ = n
            return_list.append(a)
        return return_list