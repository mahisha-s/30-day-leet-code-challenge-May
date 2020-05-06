#Python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if(i in d.keys()):
                d[i]+=1
            else:
                d[i]=1
        m=max(d.values())
        for k,v in d.items():
            if(v==m):
                return k
