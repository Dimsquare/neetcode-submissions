from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(0,len(nums)-1):
            target = -nums[i]
            temp = defaultdict(int)
            for j in range(i+1,len(nums)):
                distance = target-nums[j]
                if nums[j] in temp.keys():
                    sol = sorted([nums[i],nums[temp[nums[j]]],nums[j]])
                    if sol not in result:
                        result.append(sol)
                else:
                    temp[distance]=j
        return result