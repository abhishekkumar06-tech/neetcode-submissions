class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        ans=0
        curr=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                ans=max(ans,curr)
                curr=1
            else:
                if nums[i]-nums[i-1]==0:
                    continue
                elif nums[i]-nums[i-1]==1:
                    curr+=1
        ans=max(curr,ans)
        return ans
