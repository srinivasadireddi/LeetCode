class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
#Solution
        i=0
        n=len(nums)

        while i<n:
            if (nums[i]==val):
                nums[i]=nums[n-1]
                n-=1
            else:
                i+=1
        return n

#T: O(n)
#S: O(1)



#Attempt
        # val_indices=[]
        # n=len(nums)
        # j=0
        # i=0
        # count=0
        # j_sub_count=0
        # while count<n:
        #     while(nums[i]==val:):
        #         val_indices.append(i)
        #         i+=1
        #         count+=1
        #         j_sub_count+=1
        #     for entry in range(j_sub_count):
        #         nums[j]=val_indices[-1]
        #         val_indices.remove(val_indices[-1])
        #         j+=1
        #         i+=1
        #         count+=1
        #     j_sub_count=0
            # i+=1
            # count+=1


            
                
                

        