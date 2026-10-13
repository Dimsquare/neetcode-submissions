class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        current = 1

        for i in range(0,len(nums)):
            prefix.append(current)
            current*=nums[i]

        current = 1
        for i in range(len(nums)-1,-1,-1):
            suffix.append(current)
            current*=nums[i]

        suffix.reverse()
        res = [prefix[n]*suffix[n] for n in range(0,len(prefix))]
        return res