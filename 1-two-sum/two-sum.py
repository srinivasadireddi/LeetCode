#Srinivas
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap= {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashMap and hashMap[x] != i:
                return [i, hashMap[x]]
        #if no valid pair found, return an empty list
        return []
        