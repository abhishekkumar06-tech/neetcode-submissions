class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a=target-nums[i]
            for j in range(len(nums)):
                if a==nums[j] and i!=j:
                    return [i,j]

        
        