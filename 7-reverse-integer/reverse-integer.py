class Solution:
    def reverse(self, x: int) -> int:
        rev_str=""
        orig_x=x
        if(x<0):
            x*=-1 #then no issue with div and remainder of negative numbers
        quotient=x//10 #placeholder
        remainder=x%10 #placeholder
        while(quotient>=0):
            rev_str+=str(remainder)
            if(quotient==0):
                #return solution
                output=int(rev_str)
                if(orig_x<0):
                    output*=-1
                if(output<-2**31 or output>2**31 -1):
                    return 0
                else:
                    return output
            else:
                remainder=quotient%10
                quotient=quotient//10


        