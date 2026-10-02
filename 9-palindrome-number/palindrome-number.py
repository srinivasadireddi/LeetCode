# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s=str(x)
#         return s==s[::-1]

#Solution w/o string:
class Solution:
    def isPalindrome(self, x:int) -> bool:
        if(x<0):
            return False
        
        orig_x=x
        reversed=0
        while(x!=0):
            lastDigit= x%10
            reversed=reversed*10+lastDigit
            x=x//10
        
        return orig_x==reversed
        # if x==reversed:
        #     return True
        # else:
        #     return False