class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    #性能没加多少，可读性倒时差了，N*N*log2K
    #方法不好
     def threeSum(self, nums):

        nlen=len(nums)
        if(nlen<3):
            return []
        fnums,nmaps=self.filter(nums)
        fnums.sort()
        result=[]
        tmp=[]
        nlen=len(fnums)
        if(nlen<3):
            return []
        cur1=0
        while(cur1<nlen-2):
            if(fnums[cur1]>0):
                break
            cur2=cur1+1
            while(cur2<nlen):
                two=fnums[cur2]+fnums[cur1]
                if(two>=0 and fnums[cur2]>0):
                    break
                if([fnums[cur1], fnums[cur2]] in tmp):
                    cur2+=1
                    continue
                
                tmp+=[ [ fnums[cur1], fnums[cur2] ] ]
                tre=0-two
                if(type(nmaps.get(tre))==type(0) and tre>=fnums[cur2]):
                    if( fnums[cur1]==tre or tre==fnums[cur2]):
                        if(tre==0 and nmaps[0]>2):
                             result+=[[0,0,0]]
                        elif(tre!=0 and nmaps[tre]>1):
                             result+=[[fnums[cur1],fnums[cur2],tre]]
                    else:
                         result+=[[fnums[cur1],fnums[cur2],tre]]
                # cur3=cur2+1
                # while (cur3<nlen):
                #     if (two+fnums[cur3]>0):
                #         break
                #     if (two+fnums[cur3]==0 ):
                #         result+=[[fnums[cur1],fnums[cur2],fnums[cur3]]]
                #         break
                    
                #     cur3+=1
                cur2+=1
            cur1+=1
        return result
     def filter(self,nums):
        mp={}
        r=[]
        for num in nums:
            mp[num]=0
        for num in nums:
            mp[num]+=1
            if(mp[num]>2 and num!=0):
                continue
            r+=[num]
        return r,mp
    #性能差，N*N*N
    # def threeSum(self, nums):

    #     nlen=len(nums)
    #     if(nlen<3):
    #         return []
    #     fnums=self.filter(nums)
    #     fnums.sort()
    #     result=[]
    #     tmp=[]
    #     nlen=len(fnums)
    #     if(nlen<3):
    #         return []
    #     cur1=0
    #     while(cur1<nlen-2):
    #         if(fnums[cur1]>0):
    #             break
    #         cur2=cur1+1
    #         while(cur2<nlen):
    #             two=fnums[cur2]+fnums[cur1]
    #             if(two>=0 and fnums[cur2]>0):
    #                 break
    #             if([fnums[cur1], fnums[cur2]] in tmp):
    #                 cur2+=1
    #                 continue
                
    #             tmp+=[ [ fnums[cur1], fnums[cur2] ] ]
    #             cur3=cur2+1
    #             while (cur3<nlen):
    #                 if (two+fnums[cur3]>0):
    #                     break
    #                 if (two+fnums[cur3]==0 ):
    #                     result+=[[fnums[cur1],fnums[cur2],fnums[cur3]]]
    #                     break
                    
    #                 cur3+=1
    #             cur2+=1
    #         cur1+=1
    #     return result
    # def filter(self,nums):
    #     mp={}
    #     r=[]
    #     for num in nums:
    #         mp[num]=0
    #     for num in nums:
    #         mp[num]+=1
    #         if(mp[num]>2 and num!=0):
    #             continue
    #         r+=[num]
    #     return r
