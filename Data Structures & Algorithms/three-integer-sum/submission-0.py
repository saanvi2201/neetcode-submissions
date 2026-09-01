class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()# this sorts the array nums and stores it back into nums itself 
        result=[]
        for i in range(len(nums)-2):
            if nums[i]==nums[i-1] and i!=0:
                # what this potentially means is if the no at i and the number after it both are same then we continue the for loop and skip that i and move to the next number 
                continue
                
            k=len(nums)-1
            j=i+1
            target=-nums[i]
            while j<k:
                cur_sum=nums[j]+nums[k]
                if cur_sum>target:
                    k-=1
                elif cur_sum<target:
                    j+=1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                    while nums[k]==nums[k+1] and j<k:
                        k-=1
        return result
              