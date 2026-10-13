from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_dict = defaultdict(list)
        for i in range(0,len(strs)):
            new = [0]*26
            for m in strs[i]:
                new[ord(m)-97]+=1
            return_dict[tuple(new)].append(strs[i])
        return list(return_dict.values())
