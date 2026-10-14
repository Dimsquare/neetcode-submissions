from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = Counter()
        left = 0
        right = 0
        result = 0
        while right<len(s):
            longest[s[right]] +=1
            _,curr = longest.most_common(1)[0]
            current = sum(longest.values())
            while current-curr-k>0:
                longest[s[left]]-=1
                left+=1
                current = sum(longest.values())
            if current>result:
                result = current
            right+=1
        return result
