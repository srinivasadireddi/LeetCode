class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j,count_i=0,0,0
        while(i<len(haystack) and j<len(needle)):
            if(haystack[i]==needle[j]):
                count_i+=1
                i+=1
                j+=1
            else:
                i=i-count_i+1
                count_i=0
                j=0
            if(j==len(needle)):
                return (i-count_i)
        return -1

#T:O(n*m)
#S:O(1)
        