class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         output_s=""
#         char=s[0]
#         s_len=len(s)
#         for idx in range(s_len):
#             if (char=='V'):
#                 output_s+='5'
#                 if(idx+1>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+1]

#             elif (char=='L'):
#                 output_s+='50'
#                 if(idx+1>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+1]

#             elif (char=='D'):
#                 output_s+='500'
#                 if(idx+1>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+1]

#             elif (char=='M'):
#                 output_s+='1000'
#                 if(idx+1>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+1]
#             #I
#             elif (char=='I'):
#             #and s[idx+1]!="V" or "X"
#                 if ((idx+1<s_len) and (s[idx+1]!="V" or "X")):
#                     output_s+='1'
#                     char=s[idx+1]
#                 elif (idx+1>=s_len):
#                     return int(output_s) 



#             elif (char+s[idx+1]=='IV'):
#                 output_s+='4'
#                 if(idx+2>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+2]

#             elif (char+s[idx+1]=='IX'):
#                 output_s+='9'
#                 if(idx+2>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+2]

#             #X
#             # elif (char=='X' and s[idx+1]!="L" or "C"):
#             #     output_s+='10'
#             #     if(idx+1>=s_len):
#             #         #return output
#             #         return int(output_s)
#             #     else:
#             #         char=s[idx+1]
#             elif (char=='X'):
#             #and s[idx+1]!="V" or "X"
#                 if ((idx+1<s_len) and (s[idx+1]!="L" or "C")):
#                     output_s+='10'
#                     char=s[idx+1]
#                 elif (idx+1>=s_len):
#                     return int(output_s) 

#             elif (char+s[idx+1]=='XL'):
#                 output_s+='40'
#                 if(idx+2>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+2]
            
#             elif (char+s[idx+1]=='XC'):
#                 output_s+='90'
#                 if(idx+2>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+2]

#             #C
#             # elif (char=='C' and s[idx+1]!="D" or "M"):
#             #     output_s+='100'
#             #     if(idx+1>=s_len):
#             #         #return output
#             #         return int(output_s)
#             #     else:
#             #         char=s[idx+1]

#             elif (char=='C'):
#             #and s[idx+1]!="V" or "X"
#                 if ((idx+1<s_len) and (s[idx+1]!="D" or "M")):
#                     output_s+='100'
#                     char=s[idx+1]
#                 elif (idx+1>=s_len):
#                     return int(output_s) 

#             elif (char+s[idx+1]=='CD'):
#                 output_s+='400'
#                 if(idx+2>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+2]

#             elif (char+s[idx+1]=='CM'):
#                 output_s+='900'
#                 if(idx+2>=s_len):
#                     #return output
#                     return int(output_s)
#                 else:
#                     char=s[idx+2]
