class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        I cannot take already used 
        numList=set(nums)
        remove the element from the set and then add it back
        numList.revmove(e)
        numList.add(e)
        """
        res=[]
        n=len(nums)
        def bTracking(numsList,sol):
            #base case
            if len(sol)==n:
                res.append(sol[:])
                return
            #calculations part
            for e in nums:
                if e not in numsList:
                    sol.append(e)
                    numsList.add(e)
                    bTracking(numsList,sol)
                    sol.pop(-1)
                    numsList.remove(e)
            
        
        bTracking(set(),[])
        return res