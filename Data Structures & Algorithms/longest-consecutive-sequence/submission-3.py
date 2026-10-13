class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        idk = sorted(list(set(nums)))
        left = 0
        right = 0
        max_cons = 0

        while left+right<len(idk):
            if idk[left]+right==idk[left+right]:
                right+=1
                if right>max_cons:
                    max_cons = right
            else:
                left += right
                right = 0
        return max_cons