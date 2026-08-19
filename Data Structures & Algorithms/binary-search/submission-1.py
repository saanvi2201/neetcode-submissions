class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        
        while (l<=r):
            m=(l+r)//2 #find mid point inside the loop why ??
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m #because it means m = target
        return -1 #because this means we never found target
