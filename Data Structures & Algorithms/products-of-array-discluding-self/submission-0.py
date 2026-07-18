class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        pr=1
        c=0
        for i in nums:
            pr*=i
            if i==0:
                c+=1
            else:
                p*=i
        ans=[]
        for i in nums:
            if i==0 and c<2:
                ans.append(p)
            elif i==0 and c>1:
                ans.append(pr)
            else:
                ans.append(pr//i)

        return ans
        