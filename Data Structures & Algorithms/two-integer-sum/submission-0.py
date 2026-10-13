class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_hash = {}
        for i in range(0,len(nums)):
            diff = target-nums[i]
            if diff in difference_hash.keys():
                return [difference_hash[diff],i]
            else:
                difference_hash[nums[i]] = i