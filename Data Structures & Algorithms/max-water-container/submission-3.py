class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_area = (right-left)*min(heights[left],heights[right])
        while left<=right:
            current_area =(right-left)*min(heights[left],heights[right])
            if current_area>max_area:
                max_area = current_area
            if heights[left]>heights[right]:
                right-=1
            elif heights[right]>heights[left]:
                left+=1
            else:
                right-=1
                left+=1
        return max_area
            



