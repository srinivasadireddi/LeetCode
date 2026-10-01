#Solution:
class Solution:
    def convert(self, s:str, numRows: int) -> str:
            rows=[]




























#My solution:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lists= [ [] for _ in range(numRows) ]
        list_number=0
        str_idx=0
        list_idx=0
        ptr=s[str_idx]
        count=0
        str_len=len(s)
        while(ptr):
            #non-bridging columns
            # if (list_idx in range(0,str_len,(numRows-1))): #step_size must not be zero!
                # if (list_idx==0):
                    # if(lists[list_number][0]):
                    #     continue
                    # else:
                while (list_number <numRows):
                    lists[list_number].append(ptr)
                    if ((str_idx+1) < str_len):   #to account for the case when we cross the index after the last letter 
                        str_idx+=1
                        ptr=s[str_idx] 
                    else:
                        #return output string
                        output=""
                        for list in lists:
                            for _ in list:
                                if(_ != '#'):
                                    output+= _
                        return output


                    if(list_number<(numRows-1)):
                        list_number+=1
                    else:
                        # list_number-=1 #after we go to the last list
                        list_idx+=1
                        count=0
                        list_number=0
                        break

                #bridging columns
                while(count<numRows-2):
                    for list_number in range(0, numRows):
                        if(list_number==numRows-(count+2)):
                            lists[list_number].append(ptr)
                            if((str_idx+1) < str_len):
                                str_idx+=1
                                ptr=s[str_idx]
                            else:
                                #return output string
                                output=""
                                for list in lists:
                                    for _ in list:
                                        if(_ != '#'):
                                            output+= _
                                return output
                            
                        else:
                            lists[list_number].append('#')
                            
                    count+=1
                    list_idx+=1
                    list_number=0
        return ""        







            

        