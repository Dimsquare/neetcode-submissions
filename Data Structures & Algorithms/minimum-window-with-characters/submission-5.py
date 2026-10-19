from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        if t==s:
            return t
        lookup = Counter(t)
        l = 0
        r = 0
        shortest_substring = None
        have = 0
        need = len(lookup)
        window = defaultdict(int)
        while r<len(s):
            window[s[r]]+=1
            if s[r] in lookup and window[s[r]]==lookup[s[r]]:
                have+=1
            while have==need:
                if shortest_substring==None or r-l < len(shortest_substring):
                    shortest_substring = s[l:r+1]
                window[s[l]]-=1
                if s[l] in lookup and window[s[l]]<lookup[s[l]]:
                    have-=1
                l+=1
                
            r+=1  
        
        if shortest_substring==None:
            return ""
        return shortest_substring
            

            