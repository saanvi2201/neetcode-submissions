class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        
        #find mid point inside the loop because everytime u calc m and it has to be different based on updated l and r and if its outside while it will stay constant
        while (l<=r):
            m=(l+r)//2 
            
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m #because it means m = target
        return -1 #because this means we never found target
