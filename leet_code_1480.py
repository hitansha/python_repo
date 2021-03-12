
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums)):
            if i==0:
                r.append(nums[i])
            else:
                r.append(r[i-1]+nums[i])
        return r