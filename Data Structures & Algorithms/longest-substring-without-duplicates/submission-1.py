from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        right = 0
        temp = defaultdict()
        while right<len(s):
            while s[right] in temp.keys():
                _ = temp.pop(s[left])
                left+=1
            temp[s[right]] = right
            if (right-left)+1>max_length:
                max_length = (right-left)+1
            right+=1
        return max_length
            