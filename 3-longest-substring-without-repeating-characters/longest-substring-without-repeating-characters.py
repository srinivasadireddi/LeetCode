class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count=0
        count=0
        letters=[]

        if len(s) ==0 :
            max_count =0
            return max_count
        
        for i in range(len(s)):
            if s[i] in letters:
                letters.append(s[i])
                count+=1
                x= letters.index(s[i])
                letters=letters[x+1:]
                count = count -  (x+1)
                continue
            
            letters.append(s[i])
            count+=1
            if count > max_count:
                max_count = count
        
        return max_count

        