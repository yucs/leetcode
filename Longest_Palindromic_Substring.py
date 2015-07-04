class Solution:
    # @param {string} s
    # @return {string}
   
     rpos=0
     rlen=1
     strlen=0
     #哎 参考了网络，动态规划没想到，没状态，思路乱了。
     #第一次想到，就是考虑到从“中心向外辐射”方法，语法错误（调函数。全局变量） ，就简单的用暴力N^3方法 ，写完了，思路就乱了，“死脑筋了”。
     def longestPalindrome(self, s):
        
        #性能差。。第二天写的
        self.strlen=len(s)   
        if (self.strlen<=1):
            return s
        cur=0
        while(cur<self.strlen-1):
            left=cur-1
            right=cur+1
            self.check(s,left,right,0)
            if (s[cur]==s[right]):
                if (self.rlen==1):
                    self.rlen=2
                    self.rpos=cur
                self.check(s,left,right+1,1)
            cur+=1
        
        return s[self.rpos:self.rpos+self.rlen]
    
    
     def check(self,s,left,right,tag):
         curlen=1+tag
         while(left>=0 and right<self.strlen and s[left]==s[right]):
             left-=1
             right+=1
             curlen+=2
             if(curlen>self.rlen):
                 self.rlen=curlen
                 self.rpos=left+1
                 
             
            

        
        
        # time out.... len(s)==390 就超时了。。
        # rpos=0
        # rlen=0
        # strlen=len(s)
        # cur=0
        # while (cur<strlen-rlen):
        #     for index in range(strlen-1,cur+rlen, -1):
        #          left=cur
        #          right=index
        #          clen=index-cur
        #          while( left<right and s[left]==s[right]):
        #              left+=1
        #              right-=1
                 
        #          if (left>=right and clen>rlen):
        #               rlen=clen
        #               rpos=cur
        #               break
        #     cur+=1
        # return s[cur:cur+rlen+1]
         
