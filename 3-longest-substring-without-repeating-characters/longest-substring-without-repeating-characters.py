#Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_substring_len=0
        substr_set= set()
        for r in range(len(s)):
            while s[r] in substr_set:
                substr_set.remove(s[l])
                l+=1
            substr_set.add(s[r])
            max_substring_len= max(max_substring_len, r-l+1)
        return max_substring_len























#My solution-1: T.C: o(n^2)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_count=0
#         count=0
#         letters=[]

#         if len(s) ==0 :
#             max_count =0
#             return max_count
        
#         for i in range(len(s)):
#             if s[i] in letters:
#                 letters.append(s[i])
#                 count+=1
#                 x= letters.index(s[i])
#                 letters=letters[x+1:]
#                 count = count -  (x+1)
#                 continue
            
#             letters.append(s[i])
#             count+=1
#             if count > max_count:
#                 max_count = count
        
#         return max_count

#(In progress) My solution-2: T.C: O(n^2)    
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_count=0
#         count=0
#         # letters=[]
#         letters_dict={}

#         if len(s) ==0 :
#             max_count =0
#             return max_count
        
#         for i in range(len(s)):
#             # if s[i] in letters:
#             if s[i] in letters_dict:
#                 # letters.append(s[i])
#                 x= letters_dict.get(s[i])
#                 letters_dict.update({s[i]:i})
#                 count+=1
#                 letters_dict = {key: value for key, value in letters_dict.items() if value > x}
#                 count = count -  (x+1)
#                 continue
            
#             letters_dict.update({s[i]:i})
#             count+=1
#             if count > max_count:
#                 max_count = count
        
#         return max_count

        