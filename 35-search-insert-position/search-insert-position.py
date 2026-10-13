# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         nums_size=len(nums)
#         if(nums_size%2==0):
#             lower_bound=nums[(nums_size//2) -1]
#             upper_bound=nums[(nums_size//2)]
#         else:
#             odd_lb=nums[nums_size//2]
#             odd_ub=nums[(nums_size//2) + 1]
#         while (len(nums)%2==0 and len(nums)!=0):
#             if(target>= lower_bound and target<=upper_bound):
#                 return nums.index(upper_bound)
#             elif target<=lower_bound:
#                 nums=nums[:(len(nums)//2) -1+1]
#             elif target>=upper_bound:
#                 nums=nums[(len(nums)//2):]

#         while (len(nums)%2!=0 and len(nums)!=0):
#             if(target>= odd_lb and target<=odd_ub):
#                 return nums.index(odd_ub)
#             elif target<=odd_lb:
#                 nums=nums[:(len(nums)//2) +1-1+1]
#             elif target>=odd_ub:
#                 nums=nums[(len(nums)//2) +1-1+1:]

# #TC:O(logn)
# #S:O(1)

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left