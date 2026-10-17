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

#Solution 2
class Solution:
    def isHappy(self, n: int) -> bool:
        # set={}#this is dict!
        sett=set()
        sett.add(n)
        while(n!=1):
            str_n=str(n)
            sum_squares= sum(int(i)**2 for i in str_n)
            # if(sum_squares==1):
            #     return True
            # else:
            #     n=sum_squares
            if(sum_squares in sett):
                return False
            else:
                n=sum_squares
                sett.add(n)
        return True
#T:o(log(n))
#S:o(log(n))
