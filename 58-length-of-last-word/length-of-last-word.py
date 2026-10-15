class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        r=n-1
        count=0
        while(s[r]==" "):
            r-=1
        while(r>=0 and s[r]!=" "):
            # if(r>0):
            #     r-=1
            count+=1
            r-=1
        return count
#t:o(n)
#S:o(1)