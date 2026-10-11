class Solution:
    def myAtoi(self, s: str) -> int:
        #My ans
        #TC:O(n)
        #SC:O(n)
        final_list=[]
        final_int=0
        i=0
        sign=1

        while(i<len(s) and s[i]==" "):
                i+=1
        if(i<len(s) and s[i]=="-"):
            sign*=-1
            i+=1
        elif(i<len(s) and s[i]=="+"):
            i+=1
        while(i<len(s) and s[i]=='0'):
            i+=1
        
        while(i<len(s) and ord(s[i]) in range(48,58) ): #ascii chars corresponding to '0' to '9'
            final_list.append(int(s[i]))
            i+=1
    
        l=len(final_list)
        for i in final_list:
            final_int+=i*10**(l-1)
            l-=1
        
        output= final_int*sign
        if(output<-2**31):
            output=-2**31
        elif(output>((2**31) -1)):
            output=(2**31) -1
        
        return output
        