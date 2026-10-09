class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums) 
        j=1
        for i in range(1, n):
            if nums[i-1]!=nums[i]:
                nums[j]=nums[i]
                j+=1
        return j #last value of j is exactly equal to number of unique elements
        




        # k=0
        # encounter=[]
        # for i in range(len(nums)):
        #     if nums[i] not in encounter:
        #         encounter.append(nums[i])
        #         k+=1
        #     else:
        #         # nums[i]='_' #not needed
        #         # nums[-1]=nums[i]#overwrites last element!
        # return k