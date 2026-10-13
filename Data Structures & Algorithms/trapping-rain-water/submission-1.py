class Solution:
    def trap(self, height: List[int]) -> int:
        current_max = 0
        prefix = []
        for i in range(0,len(height)):
            prefix.append(current_max)
            if height[i]>current_max:
                current_max=height[i]
        current_max = 0
        suffix = []
        for j in range(len(height)-1,-1,-1):
            suffix.append(current_max)
            if height[j]>current_max:
                current_max=height[j]
        
        suffix.reverse()
        result = 0
        for k in range(0,len(height)):
            temp = min(prefix[k],suffix[k])-height[k]
            if temp>0:
                result+=temp
        return result