class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ans=[]
        # i=0
        # while len(strs)>i:
        #     temp=[]
        #     temp.append(strs[i])
        #     j=i+1
        #     while len(strs)>j:
        #         if sorted(strs[i])==sorted(strs[j]):
        #             temp.append(strs.pop(j))
        #         else:
        #             j+=1
        #     ans.append(temp)
        #     i+=1
        # return ans

        groups={}

        for word in strs:
            key="".join(sorted(word))
        
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        
        return list(groups.values())
        
