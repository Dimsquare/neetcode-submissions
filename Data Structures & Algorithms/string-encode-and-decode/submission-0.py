class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for n in range(0,len(strs)):
            for m in strs[n]:
                encoded_string += str(ord(m))+ " "
            encoded_string += "#"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string=[]
        temp_ord = ""
        temp_string = ""
        for char in s:
            if char==" ":
                temp_string+= chr(int(temp_ord))
                temp_ord = ""
            elif char=="#":
                decoded_string.append(temp_string)
                temp_string = ""
            else:
                temp_ord+=char
        return decoded_string