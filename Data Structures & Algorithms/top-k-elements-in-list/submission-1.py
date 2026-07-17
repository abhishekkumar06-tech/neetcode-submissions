class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        l=list(freq.items())

        l.sort(key=lambda x:x[1], reverse=True)

        result=[]
        for i in range(k):
            result.append(l[i][0])
        return result
            
        

        