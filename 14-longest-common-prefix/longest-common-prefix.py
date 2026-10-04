class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        output=""
        if "" in strs:
            return output
        if len(strs)==1:
            return strs[0]
        
        smallest_str=""
        smallest_str_len=len(strs[0]) #initialze
        for j in strs:
            if(len(j)<=smallest_str_len):
                smallest_str_len=len(j)
                smallest_str=j


        # count=0
        for i in range(len(smallest_str)):
            temp=smallest_str[i]
            for j in strs:
                if(j[i]!=temp):
                    # count+=1
                    
                # else:
                    return output
            output+=j[i]
        return output

                        

        