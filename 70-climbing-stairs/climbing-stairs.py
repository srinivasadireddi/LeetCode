# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n==1:
#             return 1 
#         if n==2:
#             return 2
#         return self.climbStairs(n-1)+self.climbStairs(n-2)
#time limit exceeded
#only 21/45 testcases passed
#feedback from leetcode:
'''
Approach
Current:
Recursion
Suggested:
Dynamic Programming
Key Idea:
Fibonacci sequence calculation using dynamic programming to avoid exponential recursion.
Consider:
Can you spot how many times climbStairs(2) gets calculated in the current tree?
'''        
#Bottom Up tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        dp=[0]*n
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]
        #TC:O(n)
        #SC:O(n)