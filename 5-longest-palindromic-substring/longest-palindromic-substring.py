class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)<=1):
            return s
        
        LPS= "" #Longest_palindromic_substring
        for i in range(1,len(s)):
            #consider odd length
            l=i
            r=i
            while(l>-1 and r<len(s)):
                if s[l]==s[r]:
                    palindrome = s[l:r+1]
                    if len(palindrome)>len(LPS):
                        LPS=palindrome
                    l-=1
                    r+=1

                else:
                    break
            
            #consider even length
            l=i-1
            r=i
            while(l>-1 and r<len(s)):
                if s[l]==s[r]:
                    palindrome = s[l:r+1]
                    if len(palindrome)>len(LPS):
                        LPS=palindrome
                    l-=1
                    r+=1

                else:
                    break
        return LPS