class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=0
        area=0 # this is the amount of water
        # water=(j - i) * min(heights[i], heights[j])
        while l<r:
            area=(r-l)*min(heights[l], heights[r])
            if area>max_area:
                max_area=area
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_area
