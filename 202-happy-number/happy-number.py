# #Solution 3
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         # to_do=True
#         l=[]
#         sum=0
#         count=0
#         while(count<=10):
#             while(n!=0):
#                 l.append(n%10)
#                 n=n//10
#             for i in l:
#                 sum+=i**2
#             if(sum==1):
#                 return True

#             else:
#                 n=sum
#                 l=[]
#                 sum=0
#                 count+=1
#         return False
# #TC:O(log(n))
# #S:O(log(n))

# #Solution 2
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         # set={}#this is dict!
#         sett=set()
#         sett.add(n)
#         while(n!=1):
#             str_n=str(n)
#             n= sum(int(i)**2 for i in str_n)
#             # if(sum_squares==1):
#             #     return True
#             # else:
#             #     n=sum_squares
#             if(n in sett):
#                 return False
#             else:
#                 # n=sum_squares
#                 sett.add(n)
#         return True
# #T:o(log(n))
# #S:o(log(n))

#Solution 1:
class Solution:
    def isHappy(self, n:int)->bool:
        def get_next(ptr):
            str_ptr=str(ptr)
            ptr= sum(int(i)**2 for i in str_ptr)
            return ptr

        fast=n
        slow=n
        
        while(fast!=1):
            slow=get_next(slow)
            fast=get_next(fast)
            fast=get_next(fast)
            if(slow==fast and fast!=1):
                return False
        return True
#T:O(logn)
#S:o(1)