class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = s.lower().replace(" ","")
        result = ""
        for r in pal:
            if ord(r) in range(48,58):
                result += r
            elif ord(r) in range(97,123):
                result += r
        if result[::-1]==result:
            return True
        else:
            return False