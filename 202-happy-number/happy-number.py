class Solution:
    def isHappy(self, n: int) -> bool:
        # to_do=True
        l=[]
        sum=0
        count=0
        while(count<=10):
            while(n!=0):
                l.append(n%10)
                n=n//10
            for i in l:
                sum+=i**2
            if(sum==1):
                return True

            else:
                n=sum
                l=[]
                sum=0
                count+=1
        return False